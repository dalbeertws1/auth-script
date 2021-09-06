
from django.contrib import admin
from django.urls import path
from core.views import home, returnScript

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('script/', returnScript, name="script"),
]
