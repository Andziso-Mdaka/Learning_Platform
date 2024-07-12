from django.db import models

class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    lecturer = models.ForeignKey('User_management.User', on_delete=models.CASCADE)
    # Add other fields as necessary

    def __str__(self):
        return self.name
