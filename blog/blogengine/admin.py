from django.contrib import admin
from blogengine.models import Post
# Register your models here.


@admin.register(Post)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]