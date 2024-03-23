from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Video)
admin.site.register(Catigore)
admin.site.register(Like)
admin.site.register(VideoCommet)
admin.site.register(Views)
admin.site.register(replyedCommet)
admin.site.register(CommetLike)