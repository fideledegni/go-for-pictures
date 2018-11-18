from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
	list_display   = ('url', 'nb_visites')
	fields = ('url', 'nb_visites')

	list_filter    = ('nb_visites',)

admin.site.register(Page, PageAdmin)
