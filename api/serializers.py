from rest_framework import serializers
from .models import Ambassador, Event, Project, InnovatorRegistration

#When using Google Drive backend, URLs automatically generate with an extra parameter so the file is downloaded
#trimDefaultURL removes the parameter, so the URL just serves the file instead of trying to download it.
def trimDefaultURL(url):
    if url.endswith("&export=download"):
        return url[:-16]
    else:
        return url

class AmbassadorSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentImages = serializers.SerializerMethodField()
    def get_contentImages(self, obj):
        urlList = []
        for image in obj.contentImages.all():
            urlList.append(trimDefaultURL(image.image.url))
        return urlList
    class Meta:
        model = Ambassador
        fields = ['pk', 'url', 'name', 'desc', 'displayImageUrl', 'contentImages']
        
class AmbassadorsListSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    class Meta:
        model = Ambassador
        fields = ['pk', 'url', 'name', 'displayImageUrl']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentVideoUrl = serializers.SerializerMethodField()
    def get_contentVideoUrl(self, obj):
        if (obj.contentVideo.name):
            return trimDefaultURL(obj.contentVideo.url)
        else:
            return None
        
    contentImages = serializers.SerializerMethodField()
    def get_contentImages(self, obj):
        urlList = []
        for image in obj.contentImages.all():
            urlList.append(trimDefaultURL(image.image.url))
        return urlList
    
    class Meta:
        model = Event
        fields = ['pk', 'url', 'name', 'date', 'desc', 'article', 'link', 'isFlagshipEvent', 'displayImageUrl', 'contentVideoUrl', 'contentImages'] #
        
    # def __init__(self, *args, **kwargs):
    #     super(EventSerializer, self).__init__(*args, **kwargs)
    #     self.fields['contentVideoUrl'].required = False

class EventsListSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    class Meta:
        model = Event
        fields = ['pk', 'url', 'name', 'date', 'isFlagshipEvent', 'displayImageUrl']
        
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentVideoUrl = serializers.SerializerMethodField()
    def get_contentVideoUrl(self, obj):
        if (obj.contentVideo.name):
            return trimDefaultURL(obj.contentVideo.url)
        else:
            return None
        
    contentImages = serializers.SerializerMethodField()
    def get_contentImages(self, obj):
        urlList = []
        for image in obj.contentImages.all():
            urlList.append(trimDefaultURL(image.image.url))
        return urlList
        
    class Meta:
        model = Project
        fields = ['pk', 'url', 'name', 'desc', 'article', 'link', 'displayImageUrl', 'contentVideoUrl', 'contentImages']
        
class ProjectsListSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    class Meta:
        model = Project
        fields = ['pk', 'url', 'name', 'displayImageUrl']
          
class InnovatorRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InnovatorRegistration
        fields = ['regIsOpen', 'regLink']