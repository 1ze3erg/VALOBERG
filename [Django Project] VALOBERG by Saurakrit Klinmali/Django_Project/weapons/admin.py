from django.contrib import admin
from .models import Weapon, Skin, Type

# Register your models here.


class design_weapon_admin(admin.ModelAdmin):
    list_display = ["name", "types", "fire_mode", "creds"]
    list_editable = ["creds"]
    list_filter = ["types"]
    ordering = ["name"]
    

class design_skin_admin(admin.ModelAdmin):
    list_display = ["collection", "weapon", "unlock"]
    list_filter = ["collection", "weapon"]
    ordering = ["collection"]
    #list_per_page = 5
    #list_editable = ["author", "category"]
    #search_fields = ["name", "author"]
    #fields = ["author", "name", "desc", "category"]


admin.site.register(Weapon, design_weapon_admin)
admin.site.register(Skin, design_skin_admin)
admin.site.register(Type)