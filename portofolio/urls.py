from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.base, name='base'),  # Hanya halaman utama (landing page)
    path('./', views.skills_view, name='skills'),
    path('../', views.portfolio, name='portfolio'),
    path('.../', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
