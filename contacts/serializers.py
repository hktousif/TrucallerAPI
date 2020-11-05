from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from contacts.models import Contacts, Names


class UserSer(ModelSerializer):
    isSpam = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'isSpam']


class RestrictMailSer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='contacts-detail', lookup_field='phone')

    class Meta:
        model = Contacts
        exclude = ['email', 'savedUsers']
        read_only_fields = ['nameList']
        depth = 1


class ContactsSer(ModelSerializer):
    name = serializers.CharField(max_length=30, required=True, write_only=True)

    class Meta:
        model = Contacts
        exclude = ['savedUsers']
        read_only_fields = ['nameList']
        depth = 1

    def create(self, validated_data):
        name, status1 = Names.objects.get_or_create(name=validated_data.pop('name'))
        request = self.context['request']
        try:
            if User.objects.filter(username=validated_data['phone']):
                serializers.ValidationError('contacts with this phone already exists.')
        except:
            pass
        obj, status2 = Contacts.objects.get_or_create(**validated_data)
        obj.savedUsers.add(request.user)
        obj.nameList.add(name)
        return obj

    def update(self, instance, validated_data):
        name, status1 = Names.objects.get_or_create(name=validated_data.pop('name'))
        instance.phone = validated_data['phone']
        instance.savedUsers.add(self.context['request'].user)
        instance.email = validated_data['email']
        instance.isSpam = validated_data['isSpam']
        instance.nameList.add(name)
        instance.save()
        return instance
