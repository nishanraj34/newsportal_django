from django.contrib import admin
from news.models import News, Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ("name",)


@admin.register(News)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','content','image','category','pub_date','created_at','created_by')
    list_display_links = ('id', 'title','content',)
    search_fields = ( 'title','content',)
    list_filter = ("category",'pub_date','created_at','created_by')
