# serializers.py
from rest_framework import serializers
from .models import LinkedInJobs

class LinkedInJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedInJobs
        fields = '__all__'
