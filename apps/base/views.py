from django.shortcuts import render
from apps.base.models import Team, Banner


# Create your views here.

def index(request):
    team = Team.objects.all()
    banner = Banner.objects.first() 
    return render(request, 'index.html', {'team_members': team, 'banner_content': banner})
