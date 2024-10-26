from django import forms

from SpeedApp.cars.models import Car


class BaseClassCarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ('owner',)

        widgets = {
            'image_url': forms.URLInput(
                attrs={'placeholder': "https://..."}
            )
        }


class CarForm(BaseClassCarForm):
    pass


class DeleteCarForm(BaseClassCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'