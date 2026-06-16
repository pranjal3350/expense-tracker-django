from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    CATEGORY_CHOICES = (
        ('Salary', 'Salary'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Rent', 'Rent'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
