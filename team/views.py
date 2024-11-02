from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import teamform
from django.shortcuts import render, redirect, get_object_or_404
from .models import teams
from django.contrib.auth.decorators import login_required



form= teamform
@login_required(login_url='/user/login')
def teamcreate(request):
     #user = request.user  
    teams_list = []  

    if request.method == 'POST':  
        form = teamform(request.POST, request.FILES)  
        if form.is_valid():  
            instance = form.save(commit=False)  
            instance.pic = request.FILES.get('image', None)  
            if instance.title in teamslist:  
                team = teams.objects.filter(title=instance.title)  
                team.delete()  

            instance.save()  
            return redirect('house:add')  # Adjust the redirect to the correct URL  
    else:  
        form = teamform()  

    # Fetch existing houses for the logged-in user  
    query = teams.objects.filter(clas=user)  

    for house in query:  
        teams_list.append(team.title)  

    return render(request, 'listofteam.html', {'form': form, 'teams_list': query})  
  
