from django.contrib import admin

from .models import Bb, Rubric



class BbAdmin(admin.ModelAdmin):
    list_display = ('author', 'poem', 'published', 'rubric')
    list_display_links = ('author', 'poem')
    search_fields = ('author', 'poem',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
    
