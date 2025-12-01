from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line
import sys

# Установите переменную окружения DJANGO_SETTINGS_MODULE
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Инициализируйте Django
import django
django.setup()

# Создайте суперпользователя
User = get_user_model()
if not User.objects.filter(username='Милена').exists():
    User.objects.create_superuser(
        username='Милена',
        email='mkkka1@yandex.ru',
        password='innovatika237'
    )
    print("Суперпользователь 'Милена' создан.")
else:
    print("Суперпользователь 'Милена' уже существует.") 
    