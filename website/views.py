from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from website.models import New, Site
from django.urls import reverse


def index(request):
    news_list = New.objects.all()
    sites_list = Site.objects.all()
    template = loader.get_template('website/index.html')
    context = {
        'news_list': news_list,
        'sites_list': sites_list
    }
    return HttpResponse(template.render(context, request))


def track(request):
    if request.method == 'POST':
        site = Site.objects.get(name=request.POST['site'])
        site.click_tracking += 1
        site.save()
        return HttpResponseRedirect(reverse('index'))
