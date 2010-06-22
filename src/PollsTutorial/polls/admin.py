'''
Created on Jun 22, 2010

@author: dpomian
'''
from PollsTutorial.polls.models import Poll
from PollsTutorial.polls.models import Choice
from django.contrib import admin

class ChoiceInline (admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin (admin.ModelAdmin):
    # fields = ['pub_date', 'question']
    list_display = ('question', 'pub_date', 'was_published_today')
    fieldsets = [
                 ('Question',         {'fields': ['question']}),
                 ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
                 ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)
