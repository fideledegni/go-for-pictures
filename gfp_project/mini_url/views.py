from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from mini_url.models import MiniURL
from .forms import MiniURLForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

"""
def create(request):
	sauvegarde = False
	if request.method == "POST":
		form = MiniURLForm(request.POST)
		if form.is_valid():
			form.save() # This saves the model instance in form
			sauvegarde = True
	else:
		form = MiniURLForm()

	return render(request, 'mini_url/create.html', {
		'form': form,
		'sauvegarde': sauvegarde
	})
"""

class URLCreate(CreateView):
	model = MiniURL
	template_name = 'mini_url/create.html'
	form_class = MiniURLForm
	success_url = reverse_lazy('show_all')
        
class URLUpdate(UpdateView):
	model = MiniURL
	template_name = 'mini_url/create.html'
	form_class = MiniURLForm
	success_url = reverse_lazy('show_all')

	def get_object(self, queryset=None):
		code = self.kwargs.get('code', None)
		return get_object_or_404(MiniURL, code=code)


	def form_valid(self, form):
		self.object = form.save()
		# Envoi d'un message à l'utilisateur
		messages.success(self.request, "Votre profil a été mis à jour avec succès.")
		return HttpResponseRedirect(self.get_success_url())



def show_all(request):
	return render(
		request,
		'mini_url/show_all.html',
		{'urls': MiniURL.objects.order_by('-nb_access')}
	)


def visit(request, code):
	to_visit = get_object_or_404(MiniURL, code=code)
	to_visit.nb_access += 1
	to_visit.save()
	return redirect(to_visit.longURL)