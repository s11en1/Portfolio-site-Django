from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя',
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Оставьте здесь свой комментарий!',
        })
    )

    class Meta:
        model = Comment
        fields = ('author', 'body')