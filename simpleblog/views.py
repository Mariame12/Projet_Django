from django.shortcuts import render,get_object_or_404
from simpleblog.models import Article, Categorie, Commentaire
from simpleblog.forms import CommentaireForm
#from django.http import HttpResponse

# Create your views here.
def homepage(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html',context={"articles":articles})

def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    commentaires = Commentaire.objects.filter(article=article.id)
    nouveauCommentaire = None
    if request.method == "POST":
        commentaireForm = CommentaireForm(data=request.POST)
        if commentaireForm.is_valid():
            nouveauCommentaire = commentaireForm.save(commit=False)
            nouveauCommentaire.article = article
            nouveauCommentaire.save()
    else:
        commentaireForm = CommentaireForm()
    return render(request, 'articles/detail.html',context={"article":article,
                                                           'commentaires': commentaires,
                                                           'nouveauCommentaire': nouveauCommentaire,
                                                           'commentaireForm': commentaireForm
                                                           })
def categ(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/index.html',context={"categories": categories})

def cat_detail(request, slug):
    cate = get_object_or_404(Categorie, slug=slug)
    return render(request, 'categories/detail_cat.html', context={"cate":cate})