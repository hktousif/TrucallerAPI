import re

from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from contacts.models import Contacts


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=30, required=True)

    def validate_username(self, username):
        if re.match(r'^\+?1?\d{9,15}$', username):
            username = get_adapter().clean_username(username)
            try:
                obj = Contacts.objects.get(phone=username)
                if obj:
                    obj.delete()
            except Contacts.DoesNotExist:
                pass
            return username
        else:
            raise serializers.ValidationError(
                "Enter valid number in the format: '+91******81'")

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('name', ''),
        }
