from django.urls import path
from .views import sview,cview,LoginView,signupview

urlpatterns = [
    # path('signup/player', playerSignUpView.as_view(), name='player_signup'),
    # path('signup/coach', coachSignUpView.as_view(), name='coach_signup'),
    path('signup/',signupview, name='signup'),
    path('home/',sview,name='home'),
    path('check',cview,name='check'),
    path('login/', LoginView.as_view(), name='login'),
    # Other URLs ...
]