from django.shortcuts import render
from .serializers import AmbassadorSerializer, AmbassadorsListSerializer, EventSerializer, EventsListSerializer, ProjectSerializer, ProjectsListSerializer, InnovatorRegistrationSerializer
from .models import Ambassador, Event, Project, InnovatorRegistration

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.
class HomeView(APIView):
    def get(self, request):
        return Response({
            "Ambassadors": reverse( "ambassador-list", request=request),
            "Events": reverse( "event-list", request=request),
            "Projects": reverse( "project-list", request=request),
            "InnovatorRegistration": reverse( "innovator-registration", request=request),
            "HomeList": reverse( "home-list", request=request)
        })

class HomeListView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Ambassador.objects.all(), 'serializer_class': AmbassadorsListSerializer},
        {'queryset': Event.objects.filter(isFlagshipEvent=True), 'serializer_class': EventsListSerializer},
        {'queryset': Project.objects.order_by('pk').reverse()[:6], 'serializer_class': ProjectsListSerializer},
        {'queryset': InnovatorRegistration.objects.all(), 'serializer_class': InnovatorRegistrationSerializer},
    ]

class AmbassadorListView(generics.ListAPIView):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorsListSerializer
class AmbassadorDetailView(generics.RetrieveAPIView):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
        
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer
class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
        
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsListSerializer
class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class InnovatorRegistrationView(generics.ListAPIView):
    queryset = InnovatorRegistration.objects.all()
    serializer_class = InnovatorRegistration