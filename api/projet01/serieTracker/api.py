from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status, mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Episode, Serie, Suivi, Vu, Utilisateur
from .serializers import SerieListSerializer, SerieFullSerializer, UtilisateurSerializer, SuiviSerializer, \
    SuiviCreationSerializer, SerieWithEpisodesSerializer, VuSerializer, UtilisateurListSerializer


class SignUpView(CreateAPIView):
    serializer_class = UtilisateurSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_model().objects.create(
            username=serializer.validated_data['username'],
            password=make_password(serializer.validated_data['password'])
        )
        token, created = Token.objects.get_or_create(user=user)

        return Response(token.key, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_data = {
            'username': user.username,
        }
        return Response(user_data, status=status.HTTP_200_OK)


class ActiveSerieListView(ListAPIView):
    serializer_class = SerieListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Serie.objects.filter(est_archive=False).order_by('nom')


class ArchiveSerieListView(ListAPIView):
    serializer_class = SerieListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Serie.objects.filter(est_archive=True).order_by('nom')


class SerieDetailView(RetrieveAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieFullSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class SerieInfoUpdateView(UpdateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class SerieEpisodesUpdateView(RetrieveUpdateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieFullSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serie = self.get_object()
        serializer = self.get_serializer(serie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class SerieCreateView(CreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class ArchiveSerieView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            serie = Serie.objects.get(pk=pk)
            serie.est_archive = True
            serie.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Serie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FollowedSeriesList(ListAPIView):
    serializer_class = SuiviSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        utilisateur = self.request.user
        return Suivi.objects.filter(utilisateur=utilisateur).select_related('serie').order_by('serie__nom')


class FollowedSeriesCreateView(CreateAPIView):
    serializer_class = SuiviCreationSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)


class FollowedSeriesDestroyView(DestroyAPIView):
    queryset = Suivi.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(utilisateur=self.request.user)


class SerieWithEpisodesRetrieveView(RetrieveAPIView):
    serializer_class = SerieWithEpisodesSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        serie_id = self.kwargs.get('id')
        try:
            return Serie.objects.get(id=serie_id)
        except Serie.DoesNotExist:
            raise NotFound('Series not found.')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['target_user'] = self.request.user
        return context


class VuCreateView(CreateAPIView):
    serializer_class = VuSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)


class VuDeleteView(DestroyAPIView):
    queryset = Vu.objects.all()
    serializer_class = VuSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class UtilisateurListView(ListAPIView):
    serializer_class = UtilisateurListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Utilisateur.objects.exclude(id=current_user.id).order_by('username')


class UtilisateurPartageListAPIView(ListAPIView):
    serializer_class = UtilisateurListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Utilisateur.objects.filter(partage_avec=current_user).order_by('username')


class AddUserToShareList(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        try:
            user_to_add = Utilisateur.objects.get(id=user_id)
            request.user.partage_avec.add(user_to_add)
            return Response({'status': 'User added to share list'}, status=status.HTTP_200_OK)
        except Utilisateur.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RemoveUserFromShareList(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        try:
            user_to_remove = Utilisateur.objects.get(id=user_id)
            request.user.partage_avec.remove(user_to_remove)
            return Response({'status': 'User removed to share list'}, status=status.HTTP_200_OK)
        except Utilisateur.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserSeriesListAPIView(ListAPIView):
    serializer_class = SerieWithEpisodesSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_user = None

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        self.target_user = Utilisateur.objects.get(id=user_id)
        suivis = Suivi.objects.filter(utilisateur=self.target_user).values_list('serie', flat=True)
        return Serie.objects.filter(id__in=suivis).prefetch_related('episodes')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['target_user'] = self.target_user
        return context
