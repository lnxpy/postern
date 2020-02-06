from django import forms
from .models import Post, AdminProfile

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('cover','title', 'content')

class Profile(forms.ModelForm):

	class Meta:
		model = AdminProfile
		fields = ('username', 'avatar', 'cover', 'first_name', 'last_name', 'bio', 'city', 'website', 'github', 'twitter')