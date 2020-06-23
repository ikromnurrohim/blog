from django import forms 
from django.contrib.auth import get_user_model 


User = get_user_model()

class RegisterForm(forms.Form):
	username		= forms.CharField()
	email 			= forms.EmailField()
	password 		= forms.CharField(widget=forms.PasswordInput())
	password2		= forms.CharField(label="Confirm Password", widget=forms.PasswordInput()) 


	# def clean_username(self):
	# 	username = self.cleaned_data.get("username")
	# 	us 		 = User.objects.filter(username=username)
	# 	if us.exists():
	# 		raise forms.ValidationError("Username is taken")
	# 	return username

	def clean_username(self):
		username 	= self.cleaned_data.get('username')
		us 			= User.objects.filter(username=username)
		if us.exists():
			raise forms.ValidationError("Username Alredy")
		return username

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	us 	  = User.objects.filter(email=email)
	# 	if us.exists():
	# 		raise forms.ValidationError("Email is already")
	# 	return email

	def clean_email(self):
		email = self.cleaned_data.get('email')
		us = User.objects.filter(email=email)
		if us.exists():
			raise forms.ValidationError("Email Alredy")
		return email

	# def clean(self):
	# 	data = self.cleaned_data
	# 	password = self.cleaned_data.get("password")
	# 	password2 = self.cleaned_data.get("password2")
	# 	if password2 != password:
	# 		raise forms.ValidationError("Password must be match")
	# 	return data


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Password Input Must be match")
		return data


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
