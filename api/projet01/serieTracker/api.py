from rest_framework.generics import ListAPIView

from .models import Serie
from .serializers import SerieSerializer


class SerieListView(ListAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
