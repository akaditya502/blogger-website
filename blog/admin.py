from re import search
from turtle import title
from django.contrib import admin
from .models import Category,post



#configurations for category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'descriptions', 'url', 'adddate')
    search_fields =('title',)


class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'cat')
    search_fields =('title',)

    list_filter =('cat',)
    list_per_page = 50
    #use  for dynamic js in admin post
    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)
    

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(post,postAdmin)
#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('title','descriptions','adddate')

