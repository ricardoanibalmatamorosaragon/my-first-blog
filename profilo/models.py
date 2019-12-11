from django.db import models
from django.utils import timezone
import json


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    terms = models.CharField(max_length=200)
    def set_terms(self, x):
        self.terms = json.dumps(x)
	
    def get_terms(self):
        return json.loads(self.terms)
