from rest_framework import serializers
from .models import USERS , EVENT_LOG , MANAGE_TICKET

class PersonalSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = USERS
        fields = ('user_id','username','password')

class EventLogSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EVENT_LOG
        fields = ('id','sid','search_name','app','owner','results_link','results','create_date')

class ManageTicketSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MANAGE_TICKET
        fields = ('ticket_id' , 'category_attack' , 'severity_id' ,'severity_name', 'assignee' , 'reporter' , 'status' , 'description' , 'create_date')