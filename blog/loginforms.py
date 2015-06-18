from django import forms


from .models import Post

class LoginForm(forms.ModelForm):
	class Meta:
       		model = Login
        	fields = ('Username', 'Password',)


