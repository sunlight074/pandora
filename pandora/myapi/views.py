from rest_framework import viewsets
from .serializers import PersonalSerializers ,EventLogSerializers , ManageTicketSerializers
from .models import USERS ,EVENT_LOG , MANAGE_TICKET

# Create your views here.

class PersonalViewset (viewsets.ModelViewSet):
    queryset = USERS.objects.all().order_by('username')
    serializer_class = PersonalSerializers

class EventLogViewset (viewsets.ModelViewSet):
    queryset = EVENT_LOG.objects.all().order_by('id')
    serializer_class = EventLogSerializers

class ManageTicketViewset (viewsets.ModelViewSet):
    queryset = MANAGE_TICKET.objects.all().order_by('ticket_id')
    serializer_class = ManageTicketSerializers
