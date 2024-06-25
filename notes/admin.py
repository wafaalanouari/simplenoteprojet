from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'created_at', 'updated_at',) #Spécifie les champs à afficher dans la liste des 
    #objets dans l'interface d'administration.
    search_fields = ('title', 'content', 'tags')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 25

admin.site.register(Note, NoteAdmin)