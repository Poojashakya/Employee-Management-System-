from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)   # Example: "John"
    last_name = models.CharField(max_length=100)    # Example: "Doe"
    email = models.EmailField(unique=True)          # Example: "john@example.com"
    department = models.CharField(max_length=100)   # Example: "Engineering"
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"