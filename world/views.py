from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, FormView
from django.views.generic.edit import SingleObjectMixin
from django.contrib.gis.geos import Point
from .models import WorldBorder, GeoPoint
from .forms import GeoPointForm

class WorldBorderView(TemplateView):
    model = WorldBorder
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super(WorldBorderView, self).get_context_data(**kwargs)
        context['form'] = GeoPointForm()
        return context

class DetailWorldBorderView(DetailView):
    model = WorldBorder
    template_name = 'map.html'

    def get_object(self):
        name_ = self.kwargs.get("name")
        return get_object_or_404(WorldBorder, name=name_)

    def get_context_data(self, **kwargs):
        context = super(DetailWorldBorderView, self).get_context_data(**kwargs)
        context['form'] = GeoPointForm()
        return context

class AddGeoPoint(FormView):
    model = WorldBorder
    form_class = GeoPointForm

    # def get_object(self):
    #     name_ = self.kwargs.get("name")
    #     return get_object_or_404(WorldBorder, name=name_)

    def get_success_url(self):
        # return reverse('map', kwargs={'name': self.object.name})
        return reverse('map_clean')

    def post(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #    return HttpResponseForbidden()
        # self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        model_instance = GeoPoint() 

        model_instance.lat = form.cleaned_data['lat']
        model_instance.lon = form.cleaned_data['lon']
        model_instance.description = form.cleaned_data['description']

        # Search for country where the added point is located
        pnt = Point(model_instance.lon, model_instance.lat)
        country = WorldBorder.objects.get(mpoly__contains=pnt)
        model_instance.country_name = country

        model_instance.save()

        return super(AddGeoPoint, self).form_valid(form)

def search_country(request):
    print(request)
    if request.method == 'GET':
        search_query = request.GET.get('search', None)
        print(search_query)
        return HttpResponseRedirect(reverse('map', kwargs={'name': search_query}))

    return HttpResponse(status=404)


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TestWorldView(TemplateView):
    template_name = 'test.html'