'''Database models for django-esign'''

from django.db import models


class compliance_checklist(models.Model):
    '''
    Quick refrence model to verify compliance steps.

    '''
    informed_consumer_record_access = models.BooleanField(default=False)

    informed_consumer_agreement_duration = models.BooleanField(default=False)

    consumer_affirmatively_consented = models.BooleanField(default=False)
