from django import forms

from RegularExam.posts.models import Post


class BaseClassPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('updated_at', 'author',)

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }

        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            }
        }


class CreatePostForm(BaseClassPostForm):
    class Meta:
        model = Post
        exclude = ('updated_at', 'author',)

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }

        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            }
        }

        help_texts = {
            'image_url': "Share your funniest furry photo URL!",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Put an attractive and unique title...'
        self.fields['content'].widget.attrs['placeholder'] = 'Share some interesting facts about your adorable pets...'


class EditPostForm(BaseClassPostForm):
    pass


class DeletePostForm(BaseClassPostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
