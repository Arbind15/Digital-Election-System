from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from login.models import Voterlist



class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email=forms.EmailField()
    class Meta:
        model=User
        # fields=['username','email','password1','password2']
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

class UserRegisterForm(forms.ModelForm):
    # DOB = forms.CharField(label='Date of Birth', widget=forms.TextInput
    # (attrs={'placeholder': 'MM/DD/YYYY'}))
    # Phone=forms.CharField(widget= forms.TextInput
    #                        (attrs={'placeholder':'+977...'}))
    # Address=forms.CharField(max_length=300)
    # Province = forms.CharField(max_length=50)
    # Gender=forms.CharField(max_length=6,widget= forms.TextInput
    #                         (attrs={'placeholder':'Male or Female or Other'}))
    #
    # # CHOICES = [('Male', 'Male'),
    # #            ('Female', 'Female'),
    # #            ('Unknown', 'Unknown')]
    # #
    # # Gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # Voter_ID_Number=forms.CharField(max_length=100)
    # Citizen_ID_Number = forms.CharField(max_length=50)
    # Photo1 = forms.ImageField(label="Photo(Candidate)")
    # Photo2 = forms.ImageField(label="Photo(Citizenship-Front)")
    # Photo3 = forms.ImageField(label="Photo(Citizenship-Rare)")


    class Meta:
        model=Voterlist
        exclude=('Remark',)
        # fields=('Phone',)
        fields=('Date_of_Birth','Address','Phone','Gender',
                'Province','Citizen_ID_Number','Photo_Candidate','Photo_Citizenship_Front','Photo_Citizenship_Rare','Voter_ID_Number')




class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=300,label='Username',widget= forms.TextInput
                           (attrs={'placeholder':'Full Name'}))
    password=forms.CharField(label="Password",max_length=32, widget=forms.PasswordInput)
    class Meta:
        model=Voterlist
        fields=['username','password']