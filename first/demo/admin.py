from django.contrib import admin
from .models import Book


# Register your models here.

#admin.site.register(Book)


#Below process actually gives more control over the class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields=['title','description']
    list_display = ['title','description']
    list_filter = ['is_published']
    search_fields = ['title']