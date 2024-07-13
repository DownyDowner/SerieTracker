from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status, mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Episode, Serie
from .serializers import SerieListSerializer, SerieFullSerializer, UtilisateurSerializer


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


class SerieDetailView(mixins.UpdateModelMixin, GenericAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieFullSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        serie = get_object_or_404(Serie, id=kwargs.get('id'))
        serializer = self.get_serializer(serie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SerieCreateView(CreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
