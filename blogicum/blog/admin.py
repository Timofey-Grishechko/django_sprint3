from django.contrib import admin
from .models import Post, Category, Location

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category',
        'pub_date', 'is_published'
    )
    list_filter = ('category', 'author')
    search_fields = ('title',)
    list_editable = ('is_published',)
