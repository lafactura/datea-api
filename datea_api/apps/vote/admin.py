from django.contrib import admin
from vote.models import Vote

class VoteAdmin(admin.ModelAdmin):
    model = Vote

admin.site.register(Vote, VoteAdmin)
