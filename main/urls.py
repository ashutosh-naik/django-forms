from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]

# from django.contrib import admin
# from django.urls import path
# from django.http import HttpResponse  # Temporary view for demonstration


# # Temporary view for the home page
# def home(request):
#     return HttpResponse("Welcome to my site!")


# urlpatterns = [
#     path("admin/", admin.site.urls),  # Keep admin pattern first
#     path("", home, name="home"),  # Home page pattern
#     path("<str:name>/", home, name="index"),  # Dynamic pattern
# ]
