from django import forms
from portfolio.models import Feedback

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "subject", "message"]
