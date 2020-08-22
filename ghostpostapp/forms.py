from django import forms
from ghostpostapp.models import BoastRoast

class BoastRoastForm(forms.Form):
    CHOICES = [(True, 'roast'), (False, 'boast')]
    isroast = forms.ChoiceField(choices=CHOICES)
    post_content =forms.CharField(max_length=280)