from django.contrib import admin

# Register your models here.
from FirstApp import models

admin.site.register(models.User)
admin.site.register(models.Article)
