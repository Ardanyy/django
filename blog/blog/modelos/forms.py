from django.views.generic.edit import CreateView,UpdateView
from django import forms
from .views import Post

class PageCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','sub','description']

class AuthorUpdate(UpdateView):
    model = Post
    fields = ['titulo','sub','description']
    template_name_suffix = '_update_form'
    