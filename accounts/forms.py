from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):  # 회원가입 폼
    password = forms.CharField(label='Password', widget=forms.PasswordInput)  # 입력되는 비밀번호가 보이지 않도록
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

    def clean_password2(self):  # 비밀번호 두번 입력받는 로직
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')  # 에러를 발생시켜라
        return cd['password2']

