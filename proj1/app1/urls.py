from django.urls import path
from .views import create_view,Show_view,Cancel_view,Update_view


urlpatterns = [
    path('create/',create_view.as_view(),name='create_url'),
    path('show/',Show_view.as_view(),name='show_url'),
    path('cancel/<int:pk>',Cancel_view.as_view(),name='cancel_url'),
    path('update/<int:pk>',Update_view.as_view(),name='update_url')
]

