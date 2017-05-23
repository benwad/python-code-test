from django.contrib import admin

from .models import ImageReaction, TweetReaction


class ImageReactionInline(admin.TabularInline):
    model = ImageReaction
    extra = 0


class TweetReactionInline(admin.TabularInline):
    model = TweetReaction
    extra = 0


admin.site.register(ImageReaction)
admin.site.register(TweetReaction)
