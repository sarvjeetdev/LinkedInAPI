# views.py
from rest_framework import generics
from .models import LinkedInJobs
from .serializers import LinkedInJobsSerializer

# GET request to list jobs, POST request to add a new job
class LinkedInJobsListCreateView(generics.ListCreateAPIView):
    queryset = LinkedInJobs.objects.all()
    serializer_class = LinkedInJobsSerializer
