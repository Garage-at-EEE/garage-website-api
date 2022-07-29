#Urls for api access

from django.urls import path, include
from .views import (
    HomeView, 
    AmbassadorListView, EventListView, ProjectListView,
    AmbassadorDetailView, EventDetailView, ProjectDetailView, 
    HomeListView, InnovatorRegistrationView
)

urlpatterns = [
    path('', HomeView.as_view(), name="api-root"),
    path('ambassadors/', AmbassadorListView.as_view(), name="ambassador-list"),
    path('events/', EventListView.as_view(), name="event-list"),
    path('projects/', ProjectListView.as_view(), name="project-list"),
    path('innovator-registration/', InnovatorRegistrationView.as_view(), name="innovator-registration"),
    
    path('ambassadors/<int:pk>', AmbassadorDetailView.as_view(), name="ambassador-detail"),
    path('events/<int:pk>', EventDetailView.as_view(), name="event-detail"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name="project-detail"),
    
    path('home/', HomeListView.as_view(), name="home-list"),
]

