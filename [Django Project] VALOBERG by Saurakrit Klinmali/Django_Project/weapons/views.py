from django.shortcuts import render, get_object_or_404
from .models import Weapon, Skin

# Create your views here.
def weapons_index(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons_index.html', {'weapons': weapons})


def weapons_detail(request, weapons_name):
    weapon = get_object_or_404(Weapon, name=weapons_name)
    return render(request, 'weapons_detail.html', {'weapon': weapon})


def skins_index(request):
    skins = Skin.objects.all()
    weapons = Weapon.objects.all()
    weapon_list={}
    for weapon in weapons:
        weapon_list[weapon.pk] = weapon.name
    return render(request, 'weapons_skins_index.html', {'skins': skins,'weapon_list': weapon_list})