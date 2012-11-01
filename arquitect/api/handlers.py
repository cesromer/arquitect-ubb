import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from data.models import Image

class BlogPostHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    fields = ('entry_title', 'entry_desc', 'entry_author', 'entry_imagen')
    #exclude = ('id', re.compile(r'^private_'))
    model = Image

    @classmethod
    def content_size(self, blogpost):
        return len(blogpost.content)

    def read(self, request, post_slug):
        post = Image.objects.get(entry_slug=post_slug)
        return post

    @throttle(5, 10*60) # allow 5 times in 10 minutes
    def update(self, request, post_slug):
        post = Image.objects.get(entry_slug=post_slug)

        post.entry_title = request.PUT.get('entry_title')
        post.save()

        return post

    def delete(self, request, post_slug):
        post = Image.objects.get(entry_slug=post_slug)

        if not request.user == post.entry_author:
            return rc.FORBIDDEN # returns HTTP 401

        post.delete()

        return rc.DELETED # returns HTTP 204

class ArbitraryDataHandler(BaseHandler):
    methods_allowed = ('GET',)

    def read(self, request, username, data):
        user = User.objects.get(username=username)

        return { 'user': user, 'data_length': len(data) }
