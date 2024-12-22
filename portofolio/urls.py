from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.base, name='base'),  # Hanya halaman utama (landing page)
    path('skills/', views.skills_view, name='skills'),
    path('portfolio/', views.portfolio, name='portfolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
