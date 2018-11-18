from django import forms
from .models import MiniURL

# Formulaire a partir d'un model...
class MiniURLForm(forms.ModelForm):
	class Meta:
		model = MiniURL
		fields = ('longURL', 'pseudo_auteur',)

