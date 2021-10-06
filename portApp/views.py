from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.http import StreamingHttpResponse, HttpResponse, HttpRequest
from wsgiref.util import FileWrapper
import mimetypes
import os

class HomeView(TemplateView):
    template_name = 'portApp/index.html'

class ProjectListView(TemplateView):
    template_name = 'portApp/list.html'

class ProjectTodoView(TemplateView):
    template_name = 'portApp/todo.html'

class ProjectCarPriceView(TemplateView):
    template_name = 'portApp/projects.html'

class ProjectCRUDView(TemplateView):
    template_name = 'portApp/CRUD.html'

class ProjectAbsentismView(TemplateView):
    template_name = 'portApp/absentism.html'

class UdemyCertificatesView(TemplateView):
    template_name = 'portApp/certificate.html'

class ContactView(TemplateView):
    template_name = 'portApp/contact.html'

class AboutView(TemplateView):
    template_name = 'portApp/about.html'

def downloadfile(request):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'MaheshDedge_DataScience_Python_Django_Resume.doc'
    filepath = base_dir + '/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Lenth'] = os.path.getsize(thefile)
    response['Content-Disposition'] ="Attachment;filename=%s" % filename
    return response
















# Create your views here.
