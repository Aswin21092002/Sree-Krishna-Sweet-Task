# sree_krishna_sweets/urls.py

from django.contrib import admin
from django.urls import path
from sweets_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complaint/', views.submit_complaint, name='submit_complaint'),
    path('complaint/status/<int:complaint_id>/', views.complaint_status, name='complaint_status'),
    path('complaint/resolve/<int:complaint_id>/', views.resolve_complaint, name='resolve_complaint'),
]
