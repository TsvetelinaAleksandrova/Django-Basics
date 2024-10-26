from django import forms

from frutipedia.fruits.models import Fruit


class BaseClassFruitForm(forms.ModelForm):

    class Meta:
        model = Fruit
        exclude = ('owner',)


class CreateFruitForm(BaseClassFruitForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        error_messages = {
            'name': {
                'unique': "This fruit name is already in use! Try a new one.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Fruit Name'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        self.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        self.fields['nutrition'].widget.attrs['placeholder'] = 'Nutrition Info'


class EditFruitForm(BaseClassFruitForm):
    pass


class DeleteFruitForm(BaseClassFruitForm):

    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'