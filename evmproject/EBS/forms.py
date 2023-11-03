from django import forms
from .models import Event,OwnerSignup,UserSignup,SponsorTbl,Category,Booking

class DateInput(forms.DateInput):
    input_type = "date"

class UpdatePasswordOwnerForm(forms.ModelForm):
    class Meta:
        model = OwnerSignup
        fields = "__all__"
        labels = {"owner.password":"Current password",}