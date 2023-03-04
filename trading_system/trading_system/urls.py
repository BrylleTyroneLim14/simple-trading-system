from django.contrib import admin
from django.urls import path
from stocks import views
# from django.urls import path, include
from django.conf.urls import url, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/place-trade/', views.PlaceTrade.as_view(), name='place_trade'),
    path('api/total-value/', views.TotalValue.as_view(), name='total_value'),
    path('test-exam/', include('stocks.urls')),
]