from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import MatchesForm,analysisform
from team.models import teams
from users.models import coachProfile
from .models import matches,analysis
def create_match(request):
    query = teams.objects.all().values()
    if request.method == 'POST':
        now = timezone.now()
        user = request.user
        coach = coachProfile.objects.get(user=user)
        form = MatchesForm(request.POST)
        if form.is_valid():
            inst=form.save(commit=False)
            inst.team1=coach.team
            if inst.isplayed:
                if  inst.date<now:
                   inst.sc1=request.POST.get('sc1')
                   inst.sc2 = request.POST.get('sc2')
                else:
                    inst.isplayed=False
                    HttpResponse("the date is set in the future")
            sv = request.POST.get('team2')
            if sv== 'notavail':
                inst.opname=request.POST.get('tname')
                m = matches.objects.filter(opname=inst.opname, date=inst.date, place=inst.place).first()
                if m is None:
                    inst.save()
            else:
                team = teams.objects.get(id=sv)
                inst.team2=team
                m=matches.objects.filter(team1=team,team2=coach.team,date=inst.date,place=inst.place).first()
                if m is None:
                  inst.save()
                else:
                  return redirect('match:addm')

            return redirect('match:show')
    else:
        form = MatchesForm()

    return render(request, 'addmatch.html', {'form': form,'teams':query})
def show(request):
    query1 = matches.objects.filter(date__lt=timezone.now()).values('team1_id', 'team2_id','opname','place', 'date','isplayed','sc1','sc2','id')
    upc = matches.objects.filter(date__gt=timezone.now()).values('team1_id', 'team2_id', 'opname', 'place', 'date')
    matches_list1 = []
    matches_list2 = []
    for m in query1:
        # Fetch the team titles based on the IDs
        team1 = teams.objects.get(id=m['team1_id'])
        team2 = teams.objects.get(id=m['team2_id']) if m['team2_id'] else None
        if m['isplayed']:
            sc1=m['sc1']
            sc2 = m['sc2']
        else:
            sc1="_"
            sc2 = "_"
        if team2 is None:
            matches_list1.append([team1.title, m['opname'], m['place'], m['date'],sc1,sc2,m['id']])  # Proper handling or "N/A" if no team2
        else:
            matches_list1.append([team1.title, team2.title, m['place'], m['date'],sc1,sc2,m['id']])
    for m in upc:
        # Fetch the team titles based on the IDs
        team1 = teams.objects.get(id=m['team1_id'])
        team2= teams.objects.get(id=m['team2_id']) if m['team2_id'] else None

        if team2 is None:
            matches_list2.append([team1.title, m['opname'], m['place'], m['date']])  # Proper handling or "N/A" if no team2
        else:
            matches_list2.append([team1.title, team2.title, m['place'], m['date']])
    return render(request, 'matches.html', {'matches': matches_list1,'upc':matches_list2})


def create_analysis(request,pk):
    item = matches.objects.get(id=pk)
    if request.method == 'POST':
        form = analysisform(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.match=item
            inst.save()
            existing = analysis.objects.filter(match=inst.match).first()
            if existing:
                existing.delete()
            inst.save()
            return redirect('match:nist')  # Adjust the redirect to the correct
    else:
        form = analysisform()
    query = analysis.objects.filter(match=item)

    return render(request, 'addanalysis.html', {'form':form,'list':query})


def nist(request):
    return render(request, 'nist.html')