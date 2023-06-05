from django.contrib import admin
from .models import Post, PostTag


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "category", "get_tags")

    def get_tags(self, obj):
        tags = obj.tags.all()
        return "\n".join([str(t) for t in tags])


admin.site.register(Post, PostAdmin)
admin.site.register(PostTag)