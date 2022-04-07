from django import forms

from simpleblog.models import Commentaire,Article

class CommentaireForm (forms.ModelForm) :
    commentaire = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'row':2}))
    #date_commentaire = forms.DateField()
    class Meta :
        model = Commentaire
        fields = ['date_commmentaire', 'commentaire', 'plus_moins']

