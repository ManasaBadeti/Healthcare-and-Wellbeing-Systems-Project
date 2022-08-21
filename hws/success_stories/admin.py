from django.contrib import admin
from .models import Success_Stories
# Register your models here.
class Success_StoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Success_Stories, Success_StoriesAdmin)

