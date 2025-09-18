from django.urls import path
from .views import about_page, category_page, cantact_page, index_page

urlpatterns = [
    path('', index_page, name="index_page"),
    path('category/', category_page, name="category_page"),
    path('contact/', cantact_page, name="contact_page"),
    path('about/', about_page, name="about_page")
]

