import os
import json
from boto.s3.connection import S3Connection
from boto.s3.key import Key

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
        filecontents = uploaded_file.read()
        new_file.write(filecontents)
        new_file.close()
        upload_to_s3(uploaded_file.name, filecontents)
        if self.request.is_ajax():
            print 'ajax!!!'
            return HttpResponse(json.dumps({'success': True}), mimetype="application/json")
        else:
            print 'not ajax!@!!'
            return super(FileUpload, self).form_invalid(form)


def upload_to_s3(filename, filecontents):
    conn = S3Connection(settings.ACCESS_KEY, settings.SECRET_KEY)
    bucket = conn.get_bucket('interviewmobileworksuploader')
    k = Key(bucket)
    k.key = filename
    k.set_contents_from_string(filecontents)


class Success(TemplateView):
    template_name = 'success.html'
