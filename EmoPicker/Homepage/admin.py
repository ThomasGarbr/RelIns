from django.contrib import admin
from .models import DataSetText

# Register your models here.
class Dst_admin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'rating')
    fields = ('text', 'rating')
    list_filter = ('rating', )

admin.site.register(DataSetText, Dst_admin)