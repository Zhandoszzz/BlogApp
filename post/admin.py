from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','get_photo','time_created','time_updated')
    list_display_links = ('title','id')
    search_fields = ('title','content','time_created')
    list_filter = ('time_created','cat')
    prepopulated_fields = {"slug":("title",)}
    def get_photo(self, object):
        if  object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width='50'>")
    get_photo.short_description = 'photo'

class CatAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name', 'id')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category, CatAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
