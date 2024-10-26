from django import forms

from SpeedApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'age': "Age requirement: 21 years and above.",
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Profile
        fields = ()