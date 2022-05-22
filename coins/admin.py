from django.contrib import admin
from .models import Coins, Consensus

# Register your models here.


class CoinsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'consensus')
    list_display_links = ('id', 'title')
    list_filter = ('consensus',)
    search_fields = ('title', 'author')


class ConsensusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Coins, CoinsAdmin)
admin.site.register(Consensus, ConsensusAdmin)

admin.site.site_title = 'Backend на Python'
admin.site.site_header = 'Управление записями'