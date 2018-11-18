from django.contrib import admin
from .models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
	list_display   = ('longURL', 'code', 'date', 'pseudo_auteur', 'nb_access')
	fields = ('longURL', 'code', 'date', 'pseudo_auteur', 'nb_access')

	list_filter    = ('pseudo_auteur',)
	date_hierarchy = 'date'
	ordering       = ('date', )
	search_fields  = ('longURL',)

admin.site.register(MiniURL, MiniURLAdmin)
