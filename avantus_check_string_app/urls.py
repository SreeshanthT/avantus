from http.client import ImproperConnectionState
from django.urls import path
from avantus_check_string_app.views import check_the_string

urlpatterns = [
    path('', check_the_string ,name="check_the_string"),
]