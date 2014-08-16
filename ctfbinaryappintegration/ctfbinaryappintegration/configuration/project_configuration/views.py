from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from iaf.integratedappsupport import IntegratedAppSupport
from iaf.iastore import IAStore
from .models import ObjectStore
from .forms import ObjectStore_form
CTF_BASE_URL = 'http://cu036.cloud.maa.collab.net'
IA_BASE_URL = 'http://10.2.0.163:8000/app/projecthome'
IA_NAME = 'Django HW'
SOAP_SESSION_KEY = 'soap_session'

def home(request):
    try :
        username, session_id, prpl_id, project_path = authenticate(request)
        response = render_to_response('configuration/project_configuration/home.html',{'home_page_message' : 'You are in project %s . \n The Integrated App Id for this project is %s' % (project_path, prpl_id),'project_path': project_path,  'iframe_url' : build_url(project_path, prpl_id), 'username': username})
        response.set_cookie(key=SOAP_SESSION_KEY, value=session_id)
        return response

    except Exception, e:
        return HttpResponseRedirect(CTF_BASE_URL)

def object_display(request):
    try :
        username, session_id, prpl_id, project_path = authenticate(request)
        try:
            objects = ObjectStore.objects.filter(object_id=request.path_info.split('/')[5])
        except ObjectStore.DoesNotExist:
            pass
        response = render_to_response('configuration/project_configuration/objects_display.html', {'objects' : objects, 'iframe_url' : build_url(project_path, prpl_id), 'username': username})
        response.set_cookie(key=SOAP_SESSION_KEY, value=session_id)
        return response

    except Exception, e:
        return HttpResponseRedirect(CTF_BASE_URL)

def object_add(request):
    try :
        username, session_id, prpl_id, project_path = authenticate(request)
        objects = ObjectStore.objects.values('object_id', 'object_title')
        print(request.method)
        if request.method == 'POST':
            form = ObjectStore_form(request.POST)
            if form.is_valid():
                ObjectStore(object_id=form.cleaned_data['object_id'], object_title=form.cleaned_data['object_title']).save()
                form = ObjectStore_form()
        else:
            form = ObjectStore_form()
        response = render_to_response('configuration/project_configuration/object_add.html', {'iframe_url' : build_url(project_path, prpl_id), 'username': username, 'objects' : objects, 'form' : form, 'project_path': project_path}, context_instance=RequestContext(request))
        response.set_cookie(key=SOAP_SESSION_KEY, value=session_id)
        return response

    except Exception, e:
        return HttpResponseRedirect(CTF_BASE_URL)

def build_url(project_path, prpl_id):
    return '%s/sf/sfmain/do/topInclude/projects.%s?linkId=%s' % (CTF_BASE_URL, project_path, prpl_id)

def authenticate(request):
    try :
        if(request.path_info.startswith('/app/projecthome')):
            project_path = request.GET.get('sfProj')
            ia_support = get_ia_support()
            #the following if loop is to remove the problem when reloading page with one time token
            if(request.COOKIES.get(SOAP_SESSION_KEY)) :
                try:
                    session_id = request.COOKIES.get(SOAP_SESSION_KEY)
                    ia_support = get_ia_support()
                    ia_support.set_soap_sessionid(session_id)
                    user_data = ia_support.get_current_user_data(session_id)
                    prpl_id = ia_support.get_link_plugid(session_id, 'projects.%s' % project_path)
                    return user_data.username, session_id, prpl_id, project_path
                except Exception, e:
                    pass
            session_id = ia_support.get_soap_sessionid_by_onetimetoken(request.GET.get('sfLoginToken'))
            ia_support.set_soap_sessionid(session_id)
            user_data = ia_support.get_current_user_data(session_id)
            prpl_id = ia_support.get_link_plugid(session_id, 'projects.%s' % project_path)
            return user_data.username, session_id, prpl_id, project_path

        elif(request.path_info.startswith('/app/projects')):
            if(request.GET.get('sfId')):
                #the following if loop is to remove the problem when reloading page with one time token
                if(request.COOKIES.get(SOAP_SESSION_KEY)) :
                    try:
                        prpl_id = request.GET.get('sfId')
                        session_id = request.COOKIES.get(SOAP_SESSION_KEY)
                        ia_support = get_ia_support()
                        ia_support.set_soap_sessionid(session_id)
                        user_data = ia_support.get_current_user_data(session_id)
                        project_path = request.path_info.split('/')[3]
                        return user_data.username, session_id, prpl_id, project_path
                    except Exception, e:
                        pass
                prpl_id = request.GET.get('sfId')
                login_token = request.GET.get('sfLoginToken')
                ia_support = get_ia_support()
                session_id = ia_support.get_soap_sessionid_by_onetimetoken(login_token)
                ia_support.set_soap_sessionid(session_id)
                user_data = ia_support.get_current_user_data(session_id)
                project_path = request.path_info.split('/')[3]
                return user_data.username, session_id, prpl_id, project_path
            else:
                session_id = request.COOKIES.get(SOAP_SESSION_KEY)
                ia_support = get_ia_support()
                ia_support.set_soap_sessionid(session_id)
                user_data = ia_support.get_current_user_data(session_id)
                project_path = request.path_info.split('/')[3]
                prpl_id = ia_support.get_link_plugid(session_id, 'projects.%s' % project_path)
                return user_data.username, session_id, prpl_id, project_path

    except Exception ,e:
        raise Exception("Authentication Error")

def get_ia_support():
    ia_support = IntegratedAppSupport()
    ia_support.set_ctf_base_url(CTF_BASE_URL)
    ia_support.set_ia_base_url(IA_BASE_URL)
    ia_support.set_integrated_app_name(IA_NAME)
    return ia_support