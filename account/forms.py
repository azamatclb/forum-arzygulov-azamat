from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=16, required=True, label='Имя пользователя')
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Потвердить пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    avatar = forms.ImageField(required=True, label='Аватарка')

    def clean(self):
        cleaned_data = super().clean()
        self.validate_username_length()
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if 'avatar' in self.files:
            user.avatar = self.files['avatar']
        if commit:
            user.save()
        return user

    def validate_username_length(self):
        username = self.cleaned_data.get('username')
        if username and not 4 <= len(username) <= 16:
            raise forms.ValidationError("Имя пользователя должно содержать от 4 до 16 символов.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'avatar']
