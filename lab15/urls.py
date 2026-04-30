from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Lab 15 жұмыс істеп тұр!</h1>
    <p><b>DEBUG:</b> """ + str(__import__('django').conf.settings.DEBUG) + """</p>
    <p><b>ALLOWED_HOSTS:</b> """ + str(__import__('django').conf.settings.ALLOWED_HOSTS) + """</p>
    <p><b>STATIC_ROOT:</b> """ + str(__import__('django').conf.settings.STATIC_ROOT) + """</p>
    <p><b>.env файлынан SECRET_KEY жүктелді:</b> ✅</p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]