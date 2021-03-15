from django.shortcuts import render, get_object_or_404
from .models import Agent, Ability, Role

# Create your views here.


def agents_index(request):
    agents = Agent.objects.all()
    ability = Ability.objects.all()
    return render(request, 'agents_index.html', {'agents': agents,'ability': ability})


def agents_detail(request, agents_name):
    agent = get_object_or_404(Agent, name=agents_name)
    return render(request, 'agents_detail.html', {'agent': agent})

