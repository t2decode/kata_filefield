from django.conf.urls import patterns, url
from kata import views

urlpatterns = patterns('',
    url(r'^$', views.UploadWizard.as_view(), name='upload'),
    url(r'^modelform/$', views.uploadModelForm, name='uploadModelForm'),
    url(r'^form/$', views.upload, name='uploadForm'),
)