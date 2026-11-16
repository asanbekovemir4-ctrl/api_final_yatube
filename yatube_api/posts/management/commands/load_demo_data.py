from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from posts.models import Comment, Follow, Group, Post

User = get_user_model()

PASSWORD = 'Yatube2025!'
USERS = (
    # (username, is_superuser)
    ('admin', True),
    ('leo', False),
    ('masha', False),
)


class Command(BaseCommand):
    help = 'Создаёт демо-данные: пользователей, группу, посты, комментарий.'

    def handle(self, *args, **options):
        users = {}
        for username, is_admin in USERS:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'is_staff': is_admin, 'is_superuser': is_admin})
            if created:
                user.set_password(PASSWORD)
                user.save()
            users[username] = user

        group, _ = Group.objects.get_or_create(
            slug='cats',
            defaults={'title': 'Котики',
                      'description': 'Всё о домашних котах'})

        if not Post.objects.exists():
            post = Post.objects.create(
                author=users['leo'], group=group,
                text='Мой кот сегодня научился открывать холодильник.')
            Post.objects.create(
                author=users['masha'],
                text='Первый пост в Yatube через API!')
            Comment.objects.create(
                author=users['masha'], post=post,
                text='Срочно вешайте замок!')

        Follow.objects.get_or_create(
            user=users['masha'], following=users['leo'])

        self.stdout.write(self.style.SUCCESS(
            'Демо-данные загружены: admin, leo, masha '
            '(пароль — в команде load_demo_data).'))
