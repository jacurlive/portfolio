from django.conf.urls.static import static
from django.urls import path

from app.views import MainView, InnerView, CustomDetailView, CustomSuccessView
from root import settings

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('inner', InnerView.as_view(), name='inner'),
    path('portfolio/<str:slug>', CustomDetailView.as_view(), name='detail'),
    path('success', CustomSuccessView.as_view(), name='success')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
