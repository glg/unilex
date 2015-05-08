from django.contrib.auth.views import logout
from django.contrib import messages
from django.template.loader import render_to_string
from vocabulary.models import Vocabulary
from utils import render

def sitemap(request):
    site = Site.objects.get_current()
    vocabularies = Vocabulary.objects.all().order_by('-updated_at')
    rendered = render_to_string('sitemap.xml', {'site':site,'vocabularies':vocabularies})
    return HttpResponse(rendered, mimetype='application/xml')

def home(request):
    return render('home.html', {}, request)

def docs(request):
    return render('docs.html', {}, request)

def logmeout(request):
    messages.success(request, '<b>Logged out.</b> Thanks for spending some quality time with the Web site today.')
    return logout(request, '/')