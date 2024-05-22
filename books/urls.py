from django.urls import path
from .views import home, add_recommendation, show_recommendations

urlpatterns = [
    path('', home, name='home'),
    path('add_recommendation/', add_recommendation, name='add_recommendation'),
    path('show_recommendations/',show_recommendations, name='show_recommendations')
]