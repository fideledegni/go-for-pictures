from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def citation(texte):
	"""
	Affiche le texte passé en paramètre, encadré de guillemets français doubles
	"""
	res = "&laquo; {} &raquo;".format(escape(texte)) # escape the text
	return mark_safe(res) # the result is safe now in order to diplay the "<<.>>""
#register.filter('citation', citation)
