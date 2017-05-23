from django.contrib import admin

from .models import Episode
from reactions.admin import ImageReactionInline, TweetReactionInline


class EpisodeAdmin(admin.ModelAdmin):
    inlines = [
        ImageReactionInline,
        TweetReactionInline
    ]


admin.site.register(Episode, EpisodeAdmin)
