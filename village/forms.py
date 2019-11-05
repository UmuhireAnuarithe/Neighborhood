from django import forms
from  .models import Profile , Business,Events
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']
    
class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        exclude = ['username']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['username']