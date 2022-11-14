from django.urls import path

from extra import views

app_name='extra'
urlpatterns = [
    path('turns-list/', views.TurnsListView.as_view(), name='turns-list'),
    path('turns/add/', views.TurnsCreateView.as_view(), name='turns-add'),
    path('turns/<int:pk>/detail', views.TurnsDetailView.as_view(), name='turns-detail'),
    path('turns/<int:pk>/update', views.TurnsUpdateView.as_view(), name='turns-update'),
    path('turns/<int:pk>/delete', views.TurnsDeleteView.as_view(), name='turns-delete'),
]