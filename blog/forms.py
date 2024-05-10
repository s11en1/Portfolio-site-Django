from django import forms

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