from django.db import models
from suppliers.models import Supplier
from questionnaires.models import Questionnaire

class Evaluation(models.Model):
   supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
   questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
   total_score = models.IntegerField()
