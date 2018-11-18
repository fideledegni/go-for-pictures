from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from blog.models import Article, Contact, Categorie
from .forms import ContactForm, NouveauContactForm
from django.views.generic import ListView, DetailView

# Home page
def home(request):
	articles = Article.objects.all() # Nous sélectionnons tous nos articles
	return render(request, 'blog/home.html', {'derniers_articles': articles})

class ListeArticles(ListView):
	model = Article
	context_object_name = "derniers_articles"
	template_name = "blog/home.html"
	paginate_by = 3

	# Pour des filtres. Soit directement de facon statique, soit dynamiquement en surchargeant get_queryset
	# queryset = Article.objects.filter(categorie__id=1)
	def get_queryset(self):
		#return Article.objects.filter(categorie__id=self.args[0]) # parametre non nomme
		id = self.kwargs.get('id', None)
		return Article.objects.filter(categorie__id=self.kwargs['id']) if id else Article.objects.all()

	def get_context_data(self, **kwargs):
		# Nous récupérons le contexte depuis la super-classe
		context = super(ListeArticles, self).get_context_data(**kwargs)
		# Nous ajoutons la liste des catégories, sans filtre particulier
		context['categories'] = Categorie.objects.all()
		return context

class LireArticle(DetailView):
	context_object_name = "article"
	model = Article
	template_name = "blog/lire.html"



def contact(request):
	# Construire le formulaire, soit avec les données postées, soit vide si l'utilisateur accède pour la première fois à la page.
	form = ContactForm(request.POST or None)

	if form.is_valid():
		sujet = form.cleaned_data['sujet']
		message = form.cleaned_data['message']
		envoyeur = form.cleaned_data['envoyeur']
		renvoi = form.cleaned_data['renvoi']
		envoi = True
	return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
	sauvegarde = False
	form = NouveauContactForm(request.POST or None, request.FILES)

	if form.is_valid():
		contact = Contact()
		contact.nom = form.cleaned_data["nom"]
		contact.photo = form.cleaned_data["photo"]
		contact.save()
		sauvegarde = True

	return render(request, 'blog/contact.html', {
		'form': form,
		'sauvegarde': sauvegarde
	})

def voir_contacts(request):
	return render(
		request,
		'blog/contacts_voir.html',
		{'contacts': Contact.objects.all()}
	)


# Articles by tag
def list_articles_by_tag(request, tag):
	return HttpResponse(
        "Vous avez demandé les articles de la catégorie {0} !".format(tag)    
    )

# Articles by dates
def list_articles(request, year, month):
	return HttpResponse(
        "Vous avez demandé les articles de {1}/{0} !".format(year, month)    
    )



def my_date(request):
	return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, number1, number2):
	total = number1 + number2
	return render(request, 'blog/addition.html', locals())