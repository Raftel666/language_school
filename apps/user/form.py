from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from apps.user.models import User


class UserFormEdit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserFormEdit, self).__init__(*args, **kwargs)
        self.fields['role'].empty_label = None

        self.fields['code'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['second_last_name'].required = False
        self.fields['email'].required = False
        self.fields['address'].required = False
        self.fields['phone'].required = False
        self.fields['role'].required = False

    class Meta:

        model = User

        fields = [
            'code',
            'first_name',
            'last_name',
            'second_last_name',
            'email',
            'address',
            'phone',
            'role',
        ]
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtcode',
                'placeholder': 'Código',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtnombre',
                'placeholder': 'Nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtapaterno',
                'placeholder': 'Apellido paterno',
            }),
            'second_last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtamaterno',
                'placeholder': 'Apellido materno',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'txtxemail',
                'placeholder': 'Correo electrónico',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtaddress',
                'placeholder': 'Dirección',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'txtphone',
                'placeholder': 'Telefono',
            }),
            'role': forms.RadioSelect(attrs={
                'class': 'form-check-input',
                'id': 'role',
            })
        }

    def clean_code(self):
        data = self.cleaned_data
        if not data['code']:
            raise ValidationError('El campo código esta vació')
        return data['code']

    def clean_first_name(self):
        data = self.cleaned_data
        if not data['first_name']:
            raise ValidationError('El campo nombre esta vació')
        return data['first_name']

    def clean_last_name(self):
        data = self.cleaned_data
        if not data['last_name']:
            raise ValidationError('El campo apellido paterno esta vació')
        return data['last_name']

    def clean_second_last_name(self):
        data = self.cleaned_data
        if not data['second_last_name']:
            raise ValidationError('El campo apellido materno esta vació')
        return data['second_last_name']

    def clean_email(self):
        data = self.cleaned_data
        if not data['email']:
            raise ValidationError('El campo correo electronico esta vacio')
        return data['email']

    def clean_address(self):
        data = self.cleaned_data
        if not data['address']:
            raise ValidationError('El campo dirección esta vació')
        return data['address']

    def clean_phone(self):
        data = self.cleaned_data
        if not data['phone']:
            raise ValidationError('El campo apellido telefono esta vació')
        return data['phone']

    def clean_role(self):
        data = self.cleaned_data
        if not data['role']:
            raise ValidationError('Debe seleccionar un rol para este usuario')
        return data['role']


class UserFormCreate(UserFormEdit):

    def __init__(self, *args, **kwargs):
        super(UserFormCreate, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password'].required = False

    class Meta(UserFormEdit.Meta):

        model = User

        fields = [
            'code',
            'password',
            'first_name',
            'last_name',
            'second_last_name',
            'email',
            'address',
            'phone',
            'role',
        ]

    def clean_password(self):
        data = self.cleaned_data
        if not data['password']:
            raise ValidationError('El campo contraseña esta vació')
        return data['password']


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Contraseña actual'
        }),
    )
    field_order = ['old_password', 'new_password1', 'new_password2']

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        }),
    )


class UpdateImage(forms.ModelForm):

    class Meta:
        model = User
        fields = ['filename', ]
        widgets = {'filename': forms.FileInput(attrs={'class': ''}), }
