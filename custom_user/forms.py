
from django import forms

import re
from custom_user.models import AuthUser
from django.utils.translation import ugettext_lazy as _




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())	
    confirm_password = forms.CharField(widget=forms.PasswordInput())
	
    class Meta:
        model = AuthUser
        fields = ('first_name','username','email','password')

    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        data=cleaned_data.get('password')
        data1=cleaned_data.get('confirm_password')
        if data!=data1:
            self.add_error('confirm_password',"Two passwords are not same")
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()
            
        return user
        
        
