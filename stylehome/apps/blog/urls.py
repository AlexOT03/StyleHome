from django.urls import path
from stylehome.apps.blog import views

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog')
]
