from django.contrib import admin
from feed.models import Member, Group, Link, Comment, Vote

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Link)
admin.site.register(Comment)
admin.site.register(Vote)
