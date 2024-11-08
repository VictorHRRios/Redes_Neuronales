from django import forms

class BirdPredictionForm(forms.Form):
    image = forms.ImageField()