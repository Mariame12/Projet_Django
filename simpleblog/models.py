from django.db import models
from unittest.util import _MAX_LENGTH
from django.urls import reverse



class User(models.Model):
    username = models.CharField(max_length=250)
    def __str__(self):
        return self.username

class Categorie(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    date_publication = models.DateTimeField('date_commentaire')
    image = models.ImageField(upload_to='categories', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.titre

    def get_success_url(self):
        return reverse('homepage', kwargs={'slug': self.object.slug})


class Article(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, )
    image = models.ImageField(upload_to='articles', null=True, blank=True)
    description = models.TextField()
    titre = models.CharField(max_length=100)
    date_de_publication = models.DateTimeField('date_de_publication')
    slug = models.SlugField(max_length=128)
    def __str__(self):
        return self.titre
    def get_success_url(self):

        return reverse('homepage', kwargs={'slug': self.object.slug})



class Commentaire(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, )
    commentaire = models.CharField(max_length=256)
    date_commmentaire = models.DateTimeField('date_commentaire')
    plus_moins = models.IntegerField(default=0)
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
