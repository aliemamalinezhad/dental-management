from rest_framework import serializers
from patient.models.patient import Patient
from users.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):

    state = serializers.JSONField()
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'id_code', 'email', 'phone', 'city', 'creator', 'state','file']


class CreatePatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
