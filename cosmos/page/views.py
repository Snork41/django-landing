from django.views.generic import ListView

from .models import Slider


class HomePageView(ListView):
    model = Slider
    template_name = 'page/index.html'
    context_object_name = 'slider'

