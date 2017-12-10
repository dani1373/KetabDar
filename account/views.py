# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("login")


def update(request):
    return HttpResponse("update")


def logout(request):
    return HttpResponse("logout")
