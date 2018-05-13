from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    # additional parameters
    path = None

    def get_context_data(self, **kwargs):
        print('path %s' % str(self.kwargs.get('path')))
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['DEBUG'] = settings.DEBUG
        return context

def user_login(request):
    context = {
        'data': 'my-data'
    }
    return render(request,'login.html', context=context)