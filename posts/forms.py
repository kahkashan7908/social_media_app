from .models import PostModel,Comment
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=('title','image','caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body','posted_by')