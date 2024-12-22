from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from .forms import playerSignUpForm, coachSignUpForm, LoginForm, PlayerProfileForm
from .models import User,playerProfile,coachProfile
from team.models import teams

def signupview(request):
    query=teams.objects.all().values()
    form1 = coachSignUpForm(request.POST)
    form2 = playerSignUpForm(request.POST)
    if request.method == "POST":
        if 'submit1' in request.POST:
            form1 = coachSignUpForm(request.POST)
            if form1.is_valid():
                sv = request.POST.get('teams1')
                inst=teams.objects.get(id=sv)
                pv= request.POST.get('pass1')
                if pv==inst.password:
                   user = form1.save()
                   login(request, user)  # Auto-login after registration
                   coachProfile.objects.create(user=user,team=inst)
                   messages.success(request, 'coach registration successful!')
                   return redirect('login')  # Change to your desired redirect page
        elif 'submit2' in request.POST:
            form2 = playerSignUpForm(request.POST)
            if form2.is_valid():
                sv = request.POST.get('teams2')
                inst = teams.objects.get(id=sv)
                pv = request.POST.get('pass2')
                if pv == inst.password:
                    user = form2.save()
                    login(request, user)  # Auto-login after registration
                    playerProfile.objects.create(user=user, team=inst)
                    messages.success(request, 'player registration successful!')
                    return redirect('login')
    return render(request, 'signup.html', {'form1': form1, 'form2': form2,'teams': query})
def sview(request):
    user = request.user
    return render(request, 'home.html',)

def cview(request):
    user = request.user
    player = playerProfile.objects.get(user=user)
    t=player.team

    return render(request, 'check.html',{'t':t})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            #ins=User.objects.get_by_natural_key(user.username)
            if user is not None and user.role == User.Role.PLAYER:
                return redirect('profile')
            elif user is not None and user.role == User.Role.COACH:
                return redirect('match:addm')
            elif user is not None and user.role == User.Role.ADMIN:
                return redirect('player_signup')
        return render(request, 'login.html', {'form': form})


def player_profile(request):
    # Assuming the playerProfile is related to the authenticated user
    player = playerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PlayerProfileForm( request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('check')  # Redirect to a success page
    else:
        form = PlayerProfileForm( instance=player)

    return render(request, 'player.html', {'form': form,'player':player})