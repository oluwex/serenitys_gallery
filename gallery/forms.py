from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ("sender_name", "sender_email", "subject", "content")

        widgets = {
            'sender_name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Your Name"}),
            'sender_email': forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Your Email"}),
            'subject': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Subject"}),
            'content': forms.Textarea(attrs={'cols': 30, 'rows': 7, 'class': "form-control", 'placeholder': "Message"}),
        }
