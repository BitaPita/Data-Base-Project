from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import path
from .views import teamcreate,showt,drillcreate,strategycreate,showstrat,dietcreate

app_name='team'
urlpatterns = [
    # path('', views.view, name='homepage'),
    # path('edithouse/<int:pk>/',views.edithouse, name='edithouse'),
    path('add/',teamcreate, name='add'),
    path('addd/',drillcreate, name='adddrill'),
    path('adds/',strategycreate, name='addstrat'),
    path('diet/',dietcreate, name='diet'),
    path('show/',showstrat,name='shows')
    # path('deletehouse/<int:pk>/', views.deletehouse, name='deletehouse')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)