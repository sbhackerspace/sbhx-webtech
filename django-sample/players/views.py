# Create your views here.
from django.shortcuts import render
from players.models import Player, AllStarTeamMember
# qs = AllStarTeamMember.objects.values('year','league').annotate(age=Avg('player__birth_year'), roster=Count('player'))

def allstar_list(request):
    # TODO - will integrate the average player bit later
    # for now just a list of years - link to roster

    allstar_years = AllStarTeamMember.objects.values_list('year', flat=True).distinct()
    return render(request, 'players/teamlist.html', {'teams': allstar_years})

def allstar_roster(request, year):
    team_members = AllStarTeamMember.objects.filter(year=year).values_list('player__name', flat=True)
    return render(request, 'players/roster.html', {'members': team_members})

