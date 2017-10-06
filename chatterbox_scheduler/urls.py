from django.conf.urls import url, include
from django.contrib import admin

from api.views.example_auth_view import ExampleView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^example/', ExampleView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls'))
]
