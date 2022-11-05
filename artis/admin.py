from django.contrib import admin
from artis.models import Artis


class ArtisAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'work_url_100')


admin.site.register(Artis, ArtisAdmin)
