# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/indexx.html')
    context = {
        'all_albums': all_albums
    }

    return render (request, 'music/index.html', context)
    # return HttpResponse(template.render(context, request))


def details(request, album_id):
    # try:
    #   album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #   raise Http404("Album Nahi Mila Bhai!")
    # or we can use this
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})