# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    ACCOUNT_STATE_CHOICES = (
        ('A', 'Active'),
        ('D', 'Disable'),
    )

    user = models.OneToOneField(User, null=False, db_index=True)

    phone_number = models.CharField(max_length=11, null=True, blank=True, default=None, db_index=True)
    age = models.PositiveIntegerField(null=True, blank=True, default=None)

    image = models.ImageField(null=True, blank=True, default=None)

    job_title = models.CharField(max_length=100, null=True, blank=True, default=None)
    education = models.CharField(max_length=50, null=True, blank=True, default=None)

    city = models.CharField(max_length=50, null=True, blank=True, default=None)
    region = models.PositiveIntegerField(null=True, blank=True, default=None)
    address = models.CharField(max_length=100, null=True, blank=True, default=None)

    state = models.CharField(max_length=1, choices=ACCOUNT_STATE_CHOICES, null=False, blank=False, default='A',
                             db_index=True)
