from django import forms

class GeoPointForm(forms.Form):
    lat = forms.FloatField()
    lon = forms.FloatField()
    description = forms.CharField()
    