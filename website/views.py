from django.http import HttpResponse
from django.template import loader
from website.models import New


def index(request):
    news_list = New.objects.all()
    template = loader.get_template('website/index.html')
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context, request))
