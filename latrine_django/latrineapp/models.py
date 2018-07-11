from django.db import models
from django.utils import timezone


class Place(models.Model):
    """Contains basic information about each facility displayed on the map."""

    organization = models.TextField(max_length=255, default='', null=True)
    website = models.TextField(max_length=255, default='', null=True)
    short_description = models.TextField(max_length=1000, default='', null=True)
    address = models.TextField(max_length=255, default='', null=False)  # required
    phone = models.TextField(max_length=20, default='', null=True)
    lat = models.FloatField(null=False)  # required
    lng = models.FloatField(null=False)  # required
    gender = models.TextField(max_length=40, default='', null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.facility_type, self.organization, self.address)

    def save(self, *args, **kwargs):
        super(Place, self).save(*args, **kwargs)


class Resource(models.Model):
    """Places can have different resources."""
    facility_type = models.CharField(max_length=255, default='', null=False)  # required
    hours = models.TextField(max_length=255, default='', null=True)
    short_description = models.TextField(max_length=1000, default='', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="resources")
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    accessible = models.NullBooleanField(default=False, null=True)
    changing_table = models.NullBooleanField(default=False, null=True)
    

class Feedback(models.Model):
    """One facility can have many types of feedback (votes and comments)."""

    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    comment = models.TextField(max_length=2000, default='', null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="feedback")
