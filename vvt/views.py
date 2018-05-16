from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views import generic
from subprocess import Popen, PIPE
from . import models
import tempfile
import os


def pa_as_pdf(request, pk):
    pa = models.ProcessingActivity.objects.get(pk=pk)
    context = {'object': pa, }
    rendered_tpl = render_to_string('vvt/processing-activities.tex', context)

    with tempfile.TemporaryDirectory() as tempdir:
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl.encode('utf-8'))
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()
    r = HttpResponse(content_type='application/pdf')
    r.write(pdf)
    return r


class IndexView(generic.ListView):
    model=models.ProcessingActivity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vvt'] = models.ProcessingActivity._meta
        return context
