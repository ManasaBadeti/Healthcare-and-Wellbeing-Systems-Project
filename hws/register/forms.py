from django.contrib.auth import authenticate, get_user_model
from django import forms
from .models import Details

User = get_user_model()


class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password"
        ]

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            "name": "email"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name": "password"})
        self.fields['confirm_password'].widget.attrs.update({
            'class': 'form-control',
            "name": "confirm_password"})

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        confirm_password = self.cleaned_data.get("confirm_password")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        SpecialSym = ['$', '@', '#', '%']

        if password != confirm_password:
            raise forms.ValidationError("Password must match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already registered")

        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("User with this username already registered")

        # you can add more validations for password

        if len(password) < 8:
            raise forms.ValidationError("Password must be greater than 8 characters")

        if password.isdigit():
            raise forms.ValidationError("Password Should not be all  numeric")

        if len(password) > 20:
            raise forms.ValidationError("Password should not be greater than 20 characters")


        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Password should have at least one numerical')


        if not any(char.isupper() for char in password):
            raise forms.ValidationError('Password should have at least one uppercase letter')


        if not any(char.islower() for char in password):
            raise forms.ValidationError('Password should have at least one lowercase letter')


        if not any(char in SpecialSym for char in password):
            raise forms.ValidationError('Password should have at least one of the symbols $, @ ,#, %')

        return super(UsersRegisterForm, self).clean(*args, **keyargs)






