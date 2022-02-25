from rest_framework import serializers
from users.models.access import Access


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = ('actions',)