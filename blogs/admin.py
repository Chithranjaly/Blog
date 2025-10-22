from django.contrib import admin

from .models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category__category_name', 'author__username',
                     'status')
    list_display = ('id', 'title', 'category', 'status', 'is_featured')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
