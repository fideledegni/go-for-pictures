from django.contrib import admin
from django.utils.text import Truncator
from .models import Categorie, Article, Contact

class ArticleAdmin(admin.ModelAdmin):
	list_display   = ('titre', 'categorie', 'auteur', 'date', 'overview')

	fieldsets = (
		# Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['collapse',],
			'fields': ('titre', 'slug', 'auteur', 'categorie')
			}),
		# Fieldset 2 : contenu de l'article
		('Contenu de l\'article', {
			'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
			'fields': ('contenu', )
			}),
		)


	list_filter    = ('auteur','categorie',)
	date_hierarchy = 'date'
	ordering       = ('date', )
	search_fields  = ('titre', 'contenu')
	prepopulated_fields = {'slug': ('titre', ), } # Pour remplir le slug automatiquement

	def overview(self, article):
		return Truncator(article.contenu).chars(40, truncate='...')

	overview.short_description = 'Aperçu du contenu'


class ContactAdmin(admin.ModelAdmin):
	list_display   = ('nom', 'adresse', 'photo',)

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact, ContactAdmin)
