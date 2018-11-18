from django.db import models
from django.utils import timezone
import random, string


class MiniURL(models.Model):
	longURL = models.URLField(unique=True, verbose_name="URL à réduire")
	code = models.CharField(max_length=10, unique=True)
	pseudo_auteur = models.CharField(max_length=42, blank=True, null=True)
	date = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
	nb_access = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Mini URL"
		verbose_name_plural = "Minis URL"

	def __str__(self):
		return "[{0}] {1}".format(self.code, self.longURL)

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.generer(7)

		super(MiniURL, self).save(*args, **kwargs)


	def generer(self, nb_caracteres):
		caracteres = string.ascii_letters + string.digits
		aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

		self.code = ''.join(aleatoire)