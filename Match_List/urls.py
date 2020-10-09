from django.urls import path
from .views import match_detail,match_summary
urlpatterns = [
    path('',match_detail),
    path('<pk>',match_summary),
]
