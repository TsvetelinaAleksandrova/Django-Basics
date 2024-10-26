from django import forms

from frutipedia.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        help_texts = {
            'password': "*Password length requirements: 8 to 20 characters",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'image_url', 'age')


class DeleteProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ()