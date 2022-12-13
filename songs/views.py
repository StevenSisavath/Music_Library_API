from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song

@api_view(['GET'])
def songs_list(request):

    return Response('ok')
