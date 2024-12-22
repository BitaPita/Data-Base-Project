from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import show,create_match,create_analysis,nist
app_name='match'
urlpatterns = [
    path('mshow/',show, name='show'),
    path('addm/',create_match,name='addm'),
    path('nist/',nist,name='nist'),
    path('analysis/<int:pk>/', create_analysis, name='analysis')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)