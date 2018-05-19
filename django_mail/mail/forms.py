from django import forms


class mailForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField()
