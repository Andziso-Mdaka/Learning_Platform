from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=[('lecturer', 'Lecturer'), ('student', 'Student')])

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.username = self.cleaned_data["email"]  # Set username to email
        if commit:
            user.save()
        return user