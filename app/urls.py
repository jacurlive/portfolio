from django.urls import path

from app.views import MainView, InnerView, PortfolioView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('inner', InnerView.as_view(), name='inner'),
    path('detail', PortfolioView.as_view(), name='portfolio')
]