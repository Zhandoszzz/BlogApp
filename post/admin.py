from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo','time_created','time_updated')
    list_display_links = ('title','id')
    search_fields = ('title','content','time_created')
    list_filter = ('time_created','cat')
    prepopulated_fields = {"slug":("title",)}

class CatAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name', 'id')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CatAdmin)
admin.site.register(Post, PostAdmin)

