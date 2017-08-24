# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums
    }

    return HttpResponse(template.render(context, request))


def details(request, album_id):
    return HttpResponse('Hello there your album id is ' + album_id)
