import os
import json

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic import TemplateView

from mobileworks.forms import FileUploadForm


class FileUpload(FormView):
    form_class = FileUploadForm
    template_name = 'simple_file_upload.html'
    success_url = 'success/'

    def form_invalid(self, form):
        print 'invalid!!!'
        print self.request.FILES
        return super(FileUpload, self).form_invalid(form)

    def form_valid(self, form):
        print self.request.FILES
        uploaded_file = self.request.FILES['qqfile']
        new_file = open(os.path.join(settings.UPLOADS, uploaded_file.name), 'w')
        new_file.write(uploaded_file.read())
        new_file.close()
        if self.request.is_ajax():
            print 'ajax!!!'
            return HttpResponse(json.dumps({'success': True}), mimetype="application/json")
        else:
            print 'not ajax!@!!'
            return super(FileUpload, self).form_invalid(form)

class Success(TemplateView):
    template_name = 'success.html'
