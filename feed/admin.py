import views
from django.contrib import admin
from models import *

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Link)
admin.site.register(Comment)
admin.site.register(Vote)
