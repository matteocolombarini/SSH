from django.contrib import admin
from .models import Questionnaire, Section, Question, Choice, QuestionnaireResponse

# Inlines semplici (un livello alla volta)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    verbose_name_plural = "Scelte"


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2
    inlines = []          # ← non mettiamo più ChoiceInline qui
    verbose_name_plural = "Domande"


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    verbose_name_plural = "Sezioni"


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']
    inlines = [SectionInline]          # Solo Sections qui
    search_fields = ['name']


# Registriamo gli altri modelli singolarmente (molto più comodo)
admin.site.register(Section)
admin.site.register(Question, admin.ModelAdmin)   # potrai aggiungere ChoiceInline qui se vuoi
admin.site.register(Choice)
admin.site.register(QuestionnaireResponse)