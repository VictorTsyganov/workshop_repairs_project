from django.views.generic.base import TemplateView


class AboutSiteView(TemplateView):
    template_name = 'about/index.html'
