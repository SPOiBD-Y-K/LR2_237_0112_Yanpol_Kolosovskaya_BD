from django.contrib import admin
from .models import Bb

@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published') # Какие поля показывать в списке
    list_filter = ('published',) # Фильтр по дате
    search_fields = ('title', 'content') # Поиск по заголовку и содержанию
# Register your models here.
