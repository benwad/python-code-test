from django.shortcuts import render
from django.views.generic import DetailView

from .models import Episode


class EpisodeDetailView(DetailView):
    template_name = 'episode_detail.html'
    model = Episode
    context_object_name = 'episode'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        image_reactions = self.object.imagereaction_set.filter(deleted=False)
        tweet_reactions = self.object.tweetreaction_set.filter(deleted=False)

        all_reactions = sorted(
            list(image_reactions) + list(tweet_reactions),
            key=lambda x: x.created_at
        )

        ctx.update({
            'reactions': all_reactions
        })

        return ctx
