# admin_dashboard/models.py
from django.db import models
import uuid

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User_management.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    table_name = models.CharField(max_length=255)
    record_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action}'
