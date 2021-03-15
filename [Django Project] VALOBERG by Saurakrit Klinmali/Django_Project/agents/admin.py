from django.contrib import admin
from .models import Agent, Ability, Role

# Register your models here.


class design_agent_admin(admin.ModelAdmin):
    list_display = ["name", "id", "role"]
    list_filter = ["role"]
    ordering = ["name"]


class design_ability_admin(admin.ModelAdmin):
    list_display = ["agent", "name", "creds", "ult_points"]
    list_filter = ["agent"]
    list_editable = ["creds"]
    ordering = ["agent"]
  

admin.site.register(Agent, design_agent_admin)
admin.site.register(Ability, design_ability_admin)
admin.site.register(Role)
