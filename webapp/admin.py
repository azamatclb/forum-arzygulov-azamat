from django.contrib import admin

from webapp.models import Topic, Comment


# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'date_created']
    list_display_links = ['id', 'summary']
    readonly_fields = ['date_created']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'date_created']
    list_display_links = ['id', 'comment']
    readonly_fields = ['date_created']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
