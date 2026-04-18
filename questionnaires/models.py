from django.db import models
from accounts.models import User


class Questionnaire(models.Model):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    TYPE_CHOICES = [
        ('radio', 'Scelta Singola'),
        ('text', 'Risposta Libera'),
    ]

    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='radio')

    def __str__(self):
        return self.text[:70]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text} ({self.score} pt)"


class QuestionnaireResponse(models.Model):
    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    total_score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Risposta Questionario"
        verbose_name_plural = "Risposte Questionari"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.supplier} - {self.questionnaire.name}"