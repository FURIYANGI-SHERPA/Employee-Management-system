from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100, null=False)
    Location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department
class Role(models.Model):
    role = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.role


class Employee(models.Model):
    First_Name = models.CharField(max_length=30, null=False)
    Last_Name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Salary = models.IntegerField(default=0)
    Bonus  = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Phone = models.IntegerField(default=0)
    Hire_Date = models.DateField()
    
    
    def __str__(self):
        return "%s %s %s" %(self.First_Name, self.Last_Name, self.Phone)