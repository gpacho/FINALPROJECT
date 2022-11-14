from django.urls import path

from pacients import views

app_name='pacients'
urlpatterns = [
    path('pacients-list/', views.PacientListView.as_view(), name='pacients-list'),
    path('pacients/add/', views.PacientCreateView.as_view(), name='pacients-add'),
    path('pacients/<int:pk>/detail', views.PacientDetailView.as_view(), name='pacients-detail'),
    path('pacients/<int:pk>/update', views.PacientUpdateView.as_view(), name='pacients-update'),
    path('pacients/<int:pk>/delete', views.PacientDeleteView.as_view(), name='pacients-delete'),
]