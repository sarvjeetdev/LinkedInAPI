# urls.py
from django.urls import path
from .views import LinkedInJobsListCreateView

urlpatterns = [
    path('jobs/', LinkedInJobsListCreateView.as_view(), name='linkedin-jobs-list-create'),
]
