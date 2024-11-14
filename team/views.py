from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import teamform, drillform
from django.shortcuts import render, redirect, get_object_or_404
from .models import teams, drill
from users.models import User,coachProfile,playerProfile
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
            if instance.title in teams_list:  
                team = teams.objects.filter(title=instance.title)  
                team.delete()   

            instance.save()  
            return redirect('team:addteam')  # Adjust the redirect to the correct URL  
    else:  
        form = teamform()  

    # Fetch existing houses for the logged-in user  
    query = teams.objects.all().values() 

    # for team in query:  
    #     teams_list.append(team.title)  

    return render(request, 'teams/addteam.html', {'form': form, 'teams_list': query})  
  

def drillcreate(request):  
    user= request.user
    coach= coachProfile.object.get(user= user)
    t = coach.team
    if request.method == 'POST':  
        form = drillform(request.POST, request.FILES)  
        if form.is_valid():  
            instance = form.save(commit=False)  
            instance.pic = request.FILES.get('pic', None)  # Get the image  
            instance.video = request.FILES.get('video', None)  # Get the video  
            instance.team = t
            # Check for existing team and delete if necessary  
            existing_drill = drill.objects.filter(title=instance.title).first()  
            if existing_drill:  
                existing_drill.delete()  

            instance.save()  
            return redirect('team:adddrill')  # Adjust the redirect to the correct URL  
    else:  
        form = drillform()  

    # Fetch existing teams  
    drill_list=[]
    query = drill.objects.filter(team=t)

    return render(request, 'teams/adddrill.html', {'form': form, 'drill_list': query}) 


def deletedrill(request, pk):
    item = drill.objects.get(id=pk)
    item.delete()
    return redirect('team:adddrill')


def editdrill(request, pk):
    drill_id = team.objects.get(id=pk)
    form = drillform(instance=drill_id)


    if request.method == "POST":
        form = drillform(request.POST, instance=drill_id)
        if form.is_valid():
            form.save()
            return redirect('team:adddrill')
    context = {'form': form}
    return render(request, 'team/adddrill.html', context)   