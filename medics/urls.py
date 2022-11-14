from django.urls import path

from medics import views

app_name='medics'
urlpatterns = [
    path('medics-list/', views.MedicListView.as_view(), name='medics-list'),
    path('medics/add/', views.MedicCreateView.as_view(), name='medics-add'),
    path('medics/<int:pk>/detail', views.MedicDetailView.as_view(), name='medics-detail'),
    path('medics/<int:pk>/update', views.MedicUpdateView.as_view(), name='medics-update'),
    path('medics/<int:pk>/delete', views.MedicDeleteView.as_view(), name='medics-delete'),
]