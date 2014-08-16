from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from iaf_endpoint.webservice.rest import resources
from iaf_endpoint.webservice.rest import urls as iaf_rest_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctfbinaryapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^api/gettest', resources.TextList.as_view()),

    # app urls
    url(r'^app/projecthome', 'configuration.project_configuration.views.home', name='home'),
    url(r'^app/projects/.*/objectid/\d+$', 'configuration.project_configuration.views.object_display', name='object_display'),
    url(r'^app/projects/.*/remaining', 'configuration.project_configuration.views.object_add', name='others'),

    # services
    url(r'service/iaf/rest/ConfigurationParameters', resources.ConfigurationParameters.as_view()),
    url(r'service/iaf/rest/ProjectConfiguration', resources.ProjectConfiguration.as_view()),
    url(r'service/iaf/rest/Title', resources.Title.as_view()),
    url(r'service/iaf/rest/ProjectId', resources.ProjectId.as_view()),

    """,
    url(r'^iaf/rest/', include(iaf_rest_urls)),
    """
)
