from django.urls import include, path
from rest_framework import routers
from .views import PersonalViewset ,ManageTicketViewset ,EventLogViewset

router = routers.DefaultRouter()
router.register('user', PersonalViewset)
router.register('manage/ticket', ManageTicketViewset)
router.register('event/log', EventLogViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]