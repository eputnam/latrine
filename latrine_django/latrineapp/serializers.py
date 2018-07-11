from .models import Place, Resource, Feedback
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('upvote', 'downvote', 'comment')


class ResourceSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer(many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Resource
        fields = ('created_at', 'updated_at', 'accessible', 'changing_table', 'facility_type', 'hours', 'short_description', 'feedback')
   

class PlaceSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = Place
        fields = ('organization', 'website', 'short_description', 'address', 'phone', 'lat', 'lng', 'gender', 'image', 'resources')
