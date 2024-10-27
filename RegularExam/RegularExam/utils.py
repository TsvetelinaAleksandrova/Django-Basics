from RegularExam.authors.models import Author
from RegularExam.posts.models import Post


def get_profile():
    return Author.objects.first()


def get_all_posts():
    return Post.objects.all() if Post.objects.all() else None