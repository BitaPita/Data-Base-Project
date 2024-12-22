from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .forms import teamform,drillform,stratform,dietform
from django.shortcuts import render, redirect, get_object_or_404
from .models import teams, drill, Strat, pos, img, diet, pic
from django.contrib.auth.decorators import login_required
from users.models import coachProfile
form = teamform


@login_required(login_url='/user/login')
def teamcreate(request):

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
            return redirect('team:add')  # Adjust the redirect to the correct URL
    else:
        form = teamform()

        # Fetch existing houses for the logged-in user
    query = teams.objects.all()

    return render(request, 'listofteam.html', {'form': form, 'teams_list': query})
def showt(request):
    query = teams.objects.all()
    return render(request, 'listofteam.html', { 'teams_list': query})


def drillcreate(request):
    user= request.user
    coach= coachProfile.objects.get(user= user)
    t = coach.team
    if request.method == 'POST':
        form = drillform(request.POST, request.FILES)
        if form.is_valid():
            dr = form.save(commit=False)
            dr.team = t
            dr.save()
            images = request.FILES.getlist('images')
            for image in images:
                pic.objects.create(image=image,drill=dr)
            uploaded_images = pic.objects.all()

            existing_drill = drill.objects.filter(title=dr.title).first()
            if existing_drill:
                existing_drill.delete()
            dr.save()
            return redirect('team:adddrill')  # Adjust the redirect to the correct URL
    else:
        form = drillform()

    query = drill.objects.filter(team=t).prefetch_related('images')
    return render(request, 'drill.html', {'form': form, 'drills': query})


def deletedrill(request, pk):
    item = drill.objects.get(id=pk)
    item.delete()
    return redirect('team:adddrill')


def editdrill(request, pk):
    drill_id = teams.objects.get(id=pk)
    form = drillform(instance=drill_id)


    if request.method == "POST":
        form = drillform(request.POST, instance=drill_id)
        if form.is_valid():
            form.save()
            return redirect('team:adddrill')
    context = {'form': form}
    return render(request, 'team/adddrill.html', context)


def strategycreate(request):
    positions = pos.objects.all()
    user = request.user
    coach = coachProfile.objects.get(user=user)
    t = coach.team
    if request.method == 'POST':
        form = stratform(request.POST)
        if form.is_valid():
            strategy = form.save(commit=False)
            strategy.team=t
            strategy.save()
            selected_positions = request.POST.getlist('positions')  # Get selected positions
            strategy.pos.set(selected_positions)

            images = request.FILES.getlist('images')
            for image in images:
                img.objects.create(image=image,strat=strategy)
            uploaded_images = img.objects.all()
           # return JsonResponse({"images": [{"url": image.image.url} for image in uploaded_images]})
            return redirect('show')
    else:
        form = stratform()

    return render(request, 'addstrat.html', {'form': form, 'positions': positions})

def showstrat(request):
    # Use prefetch_related to optimize the query for related images
    user= request.user
    coach= coachProfile.objects.get(user= user)
    t = coach.team
    strategies = Strat.objects.filter(team=t).prefetch_related('images')
    return render(request, 'stratlist.html', {'strategies': strategies})


#
def dietcreate(request):
    user= request.user
    coach= coachProfile.objects.get(user= user)
    t = coach.team
    if request.method == 'POST':
        form = dietform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.team = t
            d = diet.objects.filter(title=instance.title).first()
            if d:
                d.delete()
            instance.save()
            return redirect('home')  # Adjust the redirect to the correct URL
    else:
        form = dietform()

    # Fetch existing teams
    drill_list=[]
    query = diet.objects.filter(team=t)

    return render(request, 'adddiet.html', {'form': form, 'drill_list': query})