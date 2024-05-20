from django.urls import path
from . import views
urlpatterns = [
    path("data/",views.DataShowListCreate.as_view(),name="DataShow")
]