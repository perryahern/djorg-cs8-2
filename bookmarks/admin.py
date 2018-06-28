from django.contrib import admin
from .models import Bookmark, PrivateBookmark

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(PrivateBookmark)