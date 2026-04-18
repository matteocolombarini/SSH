from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Questionnaire, Section, QuestionnaireResponse
from suppliers.models import Supplier


def home(request):
    return render(request, 'questionnaires/home.html')


def fornitore_dashboard(request):
    questionari = Questionnaire.objects.all()
    return render(request, 'questionnaires/fornitore_dashboard.html', {
        'questionari': questionari
    })


def cliente_dashboard(request):
    questionari = Questionnaire.objects.all()
    responses = QuestionnaireResponse.objects.select_related('supplier', 'questionnaire').all()

    return render(request, 'questionnaires/cliente_dashboard.html', {
        'questionari': questionari,
        'responses': responses,
    })


def compila_questionario(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)

    sections = Section.objects.filter(questionnaire=questionnaire).prefetch_related(
        'questions__choices'
    )

    return render(request, 'questionnaires/compila_questionario.html', {
        'questionnaire': questionnaire,
        'sections': sections,
    })


def salva_risposte(request, questionnaire_id):
    if request.method == 'POST':
        questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)

        supplier = Supplier.objects.first()  # Temporaneo per test

        if not supplier:
            messages.error(request, "Errore: Nessun fornitore trovato. Creane uno dall'admin.")
            return redirect('fornitore_dashboard')

        response = QuestionnaireResponse.objects.create(
            supplier=supplier,
            questionnaire=questionnaire,
            total_score=80
        )

        messages.success(request, f"Questionario '{questionnaire.name}' inviato con successo!")
        return redirect('cliente_dashboard')

    return redirect('compila_questionario', questionnaire_id=questionnaire_id)