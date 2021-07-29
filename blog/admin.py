from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Tag, Post, Recipe, Comment


class RecipeInLine(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'create_at', 'id']
    inlines = [RecipeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, MPTTModelAdmin)
