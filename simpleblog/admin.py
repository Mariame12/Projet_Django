from django.contrib import admin
from simpleblog.models import Article, Commentaire, User,Categorie

admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(Categorie)
admin.site.register(User)
