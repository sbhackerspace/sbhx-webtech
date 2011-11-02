# Create your views here.

# qs = AllStarTeamMember.objects.values('year','league').annotate(age=Avg('player__birth_year'), roster=Count('player'))
