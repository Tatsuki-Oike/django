from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class CustomUserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label='ユーザー名',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'ユーザー名を入力してください'}),
    )

    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'パスワードを入力してください'}),
    )


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        max_length=30,
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=254,
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=mark_safe(
            "Your password can’t be too similar to your other personal information.<br>"
            "Your password must contain at least 8 characters.<br>"
            "Your password can’t be a commonly used password.<br>"
            "Your password can’t be entirely numeric."
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
