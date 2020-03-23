from django.urls import path
from .views import HomePageView, AboutPageView, DetailWorldBorderView, WorldBorderView, AddGeoPoint, search_country


urlpatterns = [
    path('map/', WorldBorderView.as_view(), name='map_clean'),
    path('map/search/', search_country, name='search_country'),
    path('map/<str:name>/', DetailWorldBorderView.as_view(), name='map'),
    path('addpoint/', AddGeoPoint.as_view(), name='addpoint'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]