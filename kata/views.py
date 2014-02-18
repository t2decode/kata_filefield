import os
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from kata.forms import MediaForm, MediaSimpleForm
from kata.models import Media

def uploadModelForm(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            print form.cleaned_data
            form.save()
            return HttpResponse("Done!")
    else:
        form = MediaForm()

    return render(request, 'kata/upload.html', {'form' : form})

def upload(request):
    if request.method == 'POST':
        form = MediaSimpleForm(request.POST, request.FILES)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponse("Done!")
    else:
        form = MediaSimpleForm()

    return render(request, 'kata/upload.html', {'form' : form})


class UploadWizard(SessionWizardView):
    form_list = [MediaSimpleForm]
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'wizard'))
    template_name = 'kata/upload_wizard.html'

    def done(self, form_list, **kwargs):
        cleaned_data = self.get_all_cleaned_data()

        media = Media(file = cleaned_data['file'])

        media.save()
        
        return HttpResponse("Done!")