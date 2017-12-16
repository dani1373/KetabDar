# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def view_list(request):
    return HttpResponse("list")


def update(request):
    return HttpResponse("update")


def info(request):
    return HttpResponse("logout")
