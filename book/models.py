# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from account.models import Account


class Book(models.Model):
    BOOK_STATE_CHOICES = (
        ('A', 'Active'),
        ('D', 'Disable'),
    )

    account = models.OneToOneField(Account, null=False, db_index=True)

    minimum_age = models.PositiveIntegerField(null=True, blank=True, default=None)
    maximum_age = models.PositiveIntegerField(null=True, blank=True, default=None)

    image = models.ImageField(null=True, blank=True, default=None)

    title = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    writer = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    genre = models.CharField(max_length=50, null=False, blank=False, db_index=True)

    keywords = models.CharField(max_length=100, null=True, blank=True, default=None)  # TODO Should change it for search

    publication_year = models.PositiveIntegerField(null=True, blank=True, default=None, db_index=True)

    height = models.PositiveIntegerField(null=True, blank=True, default=None)
    width = models.PositiveIntegerField(null=True, blank=True, default=None)

    volumes = models.PositiveIntegerField(null=True, blank=True, default=None)

    description = models.TextField(null=True, blank=True, default=None)
    summary = models.CharField(max_length=200, null=True, blank=True, default=None)

    state = models.CharField(max_length=1, choices=BOOK_STATE_CHOICES, null=False, blank=False, default='A',
                             db_index=True)
