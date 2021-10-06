from django.conf.urls import url
from . import views

app_name = 'portApp'

urlpatterns = [
    url(r'^carprice/', views.ProjectCarPriceView.as_view(), name='carprice'),
    url(r'^todo/', views.ProjectTodoView.as_view(), name='todo'),
    url(r'^projectlist/', views.ProjectListView.as_view(), name='projectlist'),
    url(r'^crud/', views.ProjectCRUDView.as_view(), name='crud'),
    url(r'^absentism/', views.ProjectAbsentismView.as_view(), name='absentism'),
    url(r'^certificate/', views.UdemyCertificatesView.as_view(), name='certificate'),
    url(r'^contact/', views.ContactView.as_view(), name='contact'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^download/', views.downloadfile, name='download'),
]
