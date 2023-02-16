from django.contrib import admin
from .models import DataSetText

# Register your models here.
class Dst_admin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'rating', 'is_garbage', 'is_estimated')
    fields = ('text', 'rating', 'is_garbage', 'is_estimated')
    list_filter = ('rating', 'is_garbage', 'is_estimated')

admin.site.register(DataSetText, Dst_admin)