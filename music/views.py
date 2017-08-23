# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

def index(request):
    return HttpResponse("Hello, world. You're at the Music index.")

def details(request, album_id):
	return HttpResponse('Hello there your album id is ' + album_id)