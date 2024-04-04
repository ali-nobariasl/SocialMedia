from django.contrib import admin

from .models import PostModel, Commment


admin.site.register(PostModel)
admin.site.register(Commment)
