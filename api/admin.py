from django import forms
from django.contrib import admin
from .models import (
    Ambassador, Event, Project,
    AmbassadorImage, EventImage, ProjectImage, InnovatorRegistration
)

class AmbassadorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Ambassador
        fields = '__all__'
class AmbassadorImageInline(admin.TabularInline):
    model = AmbassadorImage
@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    form = AmbassadorForm
    list_display = ('name', 'desc', 'displayImage')
    fields = ['name', 'desc', 'displayImage']
    inlines = [AmbassadorImageInline]


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentVideo'].required = False
    class Meta:
        model = Event
        fields = '__all__'
class EventImageInline(admin.TabularInline):
    model = EventImage
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ('name', 'date', 'desc', 'article', 'isFlagshipEvent', 'displayImage', 'contentVideo', 'link')
    fields = ['name', 'date', 'desc', 'article', 'isFlagshipEvent', 'displayImage', 'contentVideo', 'link']
    inlines = [EventImageInline]

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentVideo'].required = False
    class Meta:
        model = Project
        fields = '__all__'
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'desc', 'article', 'displayImage', 'contentVideo', 'link')
    fields = ['name', 'desc', 'article', 'displayImage', 'contentVideo', 'link']  
    inlines = [ProjectImageInline]

admin.site.register(InnovatorRegistration)