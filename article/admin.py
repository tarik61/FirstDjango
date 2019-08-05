from django.contrib import admin

from .models import Article,Comment

# Register your models here.
#admin.register(Article)

@admin.register(Article)
class Articleadmin(admin.ModelAdmin):

    list_display = ["title","autor","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Article
admin.site.register(Comment)