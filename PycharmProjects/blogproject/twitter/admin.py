from django.contrib import admin
from models import  Tweet, Amicizia
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ["title", "user"]
    date_hierarchy = "created"
    search_fields = ["title"]

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Amicizia)

