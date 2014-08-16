from ctfbinaryappintegration.configuration.project_configuration import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer,JSONRenderer,XMLRenderer
from iaf.iatypes import GetConfigurationParametersResponse, \
                                    ConfigurationParameter, \
                                    GetTitleResponse, \
                                    GetProjectIdResponse
from django.http import HttpResponse
from ctfbinaryappintegration.iaf_endpoint.webservice.rest.renderers import CustomXMLRenderer

MIMETYPE = 'application/xml'
CONTENT_TYPE = 'application/xml'


class ConfigurationParameters(APIView):
    renderer_classes = [CustomXMLRenderer]

    def get(self, request, format=None):
        response = GetConfigurationParametersResponse()
        return HttpResponse(response.toxml(), mimetype=MIMETYPE, status=200, content_type=CONTENT_TYPE)

class ProjectConfiguration(APIView):
    renderer_classes = [CustomXMLRenderer]

    def post(self, request, format=None):
        return HttpResponse(mimetype=MIMETYPE, status=200, content_type=CONTENT_TYPE)

    def put(self, request, format=None):
        response = GetConfigurationParametersResponse()
        return HttpResponse(mimetype=MIMETYPE, status=204, content_type=CONTENT_TYPE)

    def delete(self, request, format=None):
        response = GetConfigurationParametersResponse()
        return HttpResponse(mimetype=MIMETYPE, status=204, content_type=CONTENT_TYPE)

class Title(APIView):
    renderer_classes = [CustomXMLRenderer]

    def get(self, request, format=None):
        response = GetTitleResponse()
        try:
            object_title = models.ObjectStore.objects.get(object_id=request.path_info.split('/')[6]).object_title
        except models.ObjectStore.DoesNotExist:
            raise Exception("Invalid object")
        response.title = object_title
        return HttpResponse(response.toxml(), mimetype=MIMETYPE, status=200, content_type=CONTENT_TYPE)

class ProjectId(APIView):
    renderer_classes = [CustomXMLRenderer]

    def get(self, request, format=None):
        response = GetProjectIdResponse()
        response.projectId = 'proj1001'
        return HttpResponse(response.toxml(), mimetype=MIMETYPE, status=200, content_type=CONTENT_TYPE)