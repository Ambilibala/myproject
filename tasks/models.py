from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)
#     app_label = 'tasks'

#     def __str__(self):
#         return self.title
# # 
# class Task(models.Model):
#     app_label = 'tasks'
#     # ... rest of the model definition ...
from django.db import models

class Task(models.Model):
    app_label = 'tasks'
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title