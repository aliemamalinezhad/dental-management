from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers.access import AccessSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    access = AccessSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'role','perm','access',
            'is_superuser', 'perm', 'id_code','phone',
        )


