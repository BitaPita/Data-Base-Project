from django.urls import path
from .views import sview,cview,LoginView,signupview,player_profile

urlpatterns = [
    # path('signup/player', playerSignUpView.as_view(), name='player_signup'),
    path('signup/',signupview, name='signup'),
    path('home/',sview,name='home'),
    path('check/',cview,name='check'),
    path('profile/',player_profile,name='profile'),
    path('login/', LoginView.as_view(), name='login'),
]