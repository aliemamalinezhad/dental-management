from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


# Create your views here.

class GetAllApiView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            srz_data = UserSerializer(users, many=True).data
            return Response(
                {'data': srz_data},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'Internal Server Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
