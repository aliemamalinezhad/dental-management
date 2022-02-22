from patient.models.patient import Patient
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer,CreatePatientSerializer


class GetAllAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            all_patients = Patient.objects.all().order_by('-create_at')
            # print(all_patients)
            # data = []
            #
            # for patient in all_patients:
            #     print(type(patient.state))
            #     data.append({
            #         "first_name": patient.first_name,
            #         "last_name": patient.last_name,
            #         "email": patient.email,
            #         "phone": patient.phone,
            #         "creator": f'{patient.creator.first_name} {patient.creator.last_name}',
            #         "created_at": patient.create_at,
            #         "access": patient.state,
            #     })

            srz_data = PatientSerializer(all_patients, many=True).data
            return Response({'data': srz_data}, status=status.HTTP_200_OK)
        except:
            return Response({'data': 'Internal Server Error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )


class CreateApiView(APIView):

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
