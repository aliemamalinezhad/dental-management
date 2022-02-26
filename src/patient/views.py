from patient.models.patient import Patient
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer, CreatePatientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from permision.patient import AuthorAllStaffAllButEditOrReadOnly


class GetAllAPIView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            all_patients = Patient.objects.all().order_by('-create_at')

            srz_data = PatientSerializer(all_patients, many=True).data
            return Response({'data': srz_data}, status=status.HTTP_200_OK)
        except:
            return Response({'data': 'Internal Server Error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )


class CreateApiView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = CreatePatientSerializer(data=request.data)
        try:
            if data.is_valid():
                data.save()
                return Response({'data': data.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            print(data.data)

            return Response(
                data.errors,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdatePatientApiView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly,]
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        srz_data = CreatePatientSerializer(instance=patient, data=request.data, partial=True)
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
