from django.urls import path
from .views import  teamcreate, drillcreate, deletedrill, editdrill
app_name= 'team'
urlpatterns = [
    path('addteam/', teamcreate, name='addteam'),
    path('adddrill/', drillcreate, name='adddrill'),
    path('editdrill/<int:pk>/',editdrill, name='editdrill'),
    path('deletedrill/<int:pk>/', deletedrill, name='deletedrill')
]