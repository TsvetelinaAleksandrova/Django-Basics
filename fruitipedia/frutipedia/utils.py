from frutipedia.fruits.models import Fruit
from frutipedia.profiles.models import Profile


def get_user_obj():
    return Profile.objects.first()


def get_all_fruits():
    return Fruit.objects.all() if Fruit.objects.all() else None