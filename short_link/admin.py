from django.contrib import admin
from short_link.models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass

