from django import forms 
from .models import Review_message
from .models import Comment


class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={
        'class': 'input-field', 'name': 'name'
    }))
    email = forms.CharField(max_length = 250, widget=forms.EmailInput(attrs={
        'class': 'input-field', 'name': 'email'
    }))
    subject = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={
        'class': 'input-field', 'name': 'subject'
    }))
    message = forms.CharField(max_length = 250, widget=forms.Textarea(attrs={
        'class': 'input-field textarea-field', 'rows': 5, 'name': 'message'
    }))
    class Meta:
        model = Review_message
        fields = ['name', 'email','subject','message']


class CommentForm(forms.ModelForm):
    commenter = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder':'Name'
    }))
    body = forms.CharField(max_length = 250, widget=forms.Textarea(attrs={
        'class': 'input-field textarea-field', 'rows': 5, 'placeholder':'Your Comment'
    }))
    class Meta:
        model = Comment
        fields = ['commenter', 'body']        