from django import forms
from TravelDetails.models.TravelRequest import TravelRequest


class TravelRequestForm(forms.ModelForm):
    
    class Meta:
        model = TravelRequest
        fields = "__all__"