from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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


class CreateUserApiView(APIView):
    def post(self, request):
        data = UserSerializer(data=request.data)
        try:
            if data.is_valid():
                data.save()
                return Response(
                    {'data': data.data},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'status': 'Bad Request'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'Error': data.errors},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateUserApiView(APIView):
    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        srz_data = UserSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(
                {'data': srz_data.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {'data': srz_data.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class DeleteUserApiView(APIView):
    def delete(self, request, username):
        user = get_object_or_404(User, username=username)
        user.delete()
        return Response(
            {'status': 'Item deleted successfully'},
            status=status.HTTP_204_NO_CONTENT,
        )
