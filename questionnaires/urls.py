from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # ← Home page
    path('fornitori/', views.fornitore_dashboard, name='fornitore_dashboard'),
    path('client/', views.cliente_dashboard, name='cliente_dashboard'),
    path('compila/<int:questionnaire_id>/', views.compila_questionario, name='compila_questionario'),
    path('salva-risposte/<int:questionnaire_id>/', views.salva_risposte, name='salva_risposte'),
]