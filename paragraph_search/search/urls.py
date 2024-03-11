from django.urls import path
from . import views

urlpatterns = [
    path('paragraphs/', views.ParagraphCreateView.as_view(), name='paragraph-create'),
    path('search/', views.ParagraphSearchView.as_view(), name='paragraph-search'), 
]
