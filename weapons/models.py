from django.db import models

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("rejected", "Rejected"),
    ("processed", "Processed"),
]


class Request(models.Model):
    agent_identifier = models.CharField(max_length=255)
    assignment_service = models.CharField(max_length=255)
    agent_phone_number = models.CharField(max_length=16)
    agent_email = models.EmailField()
    weapon_type = models.CharField(max_length=255)
    weapon_length = models.IntegerField()
    weapon_barrel_length = models.IntegerField()
    picture_left = models.FileField()
    picture_right = models.FileField()
    picture_markings = models.FileField()
    picture_charger = models.FileField()
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0]
    )
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Analysis(models.Model):
    class Meta:
        verbose_name_plural = "Analyses"

    picture = models.FileField()
    label = models.CharField(max_length=255)
    confidence = models.DecimalField(max_digits=10, decimal_places=9)
    created = models.DateTimeField(auto_now_add=True)
