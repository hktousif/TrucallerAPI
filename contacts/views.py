from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from contacts.models import Contacts
from contacts.serializers import ContactsSer, RestrictMailSer, UserSer


class ContactView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    lookup_field = 'phone'

    # filter_backends = [DjangoFilterBackend, SearchFilter, filters.OrderingFilter]
    # search_fields = ['phone', 'nameList__name']
    def get_permissions(self):
        if self.action in ['destroy', 'list']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list', 'search']:
            return RestrictMailSer
        else:
            return ContactsSer

    def retrieve(self, request, phone=None):
        contact = Contacts.objects.get(phone=phone)
        serializer = self.get_serializer(contact)
        if request.user in contact.savedUsers.all():
            with_mail = serializer.data
            with_mail['email'] = contact.email
            return Response(with_mail, status=200)
        return Response(serializer.data, status=200)

    @action(detail=False)
    def search(self, request):
        search = request.GET.get('value', '').strip()
        try:
            registered_user = User.objects.get(username=search)
            user_ser = UserSer(registered_user, context={'request': request})
            return Response(user_ser.data, status=200)
        except User.DoesNotExist:
            queryset = self.get_queryset()
            contact = queryset.filter(Q(phone=search) | Q(nameList__name__icontains=search)).distinct()
            serializer = self.get_serializer(contact, many=True)
            return Response(serializer.data, status=200)
        except:
            Response(status=400)
