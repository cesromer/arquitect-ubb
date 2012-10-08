from django import forms

class ContactForm(forms.Form):
    Email       = forms.EmailField(widget=forms.TextInput())
    Titulo      = forms.CharField(widget=forms.TextInput())
    Cuerpo      = forms.CharField(widget=forms.Textarea())
