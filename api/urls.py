from django.urls import path
from . import views

urlpatterns = [
    path('headlar/',views.head),
    path('portfoliolar/',views.portfolio),
    path('teamlar/',views.team),
    path('vakansiyalar/',views.vakansiya),
    path('post/message/',views.post_message),
    path('post/resume/',views.post_resume),
]