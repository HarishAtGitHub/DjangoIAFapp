#from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url, include
import resources
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^ConfigurationParameters', resources.ConfigurationParameters.as_view()),
    url(r'^ProjectConfiguration', resources.ProjectConfiguration.as_view()),
    url(r'^Title', resources.Title.as_view()),
    url(r'^ProjectId', resources.ProjectId.as_view()),
)

