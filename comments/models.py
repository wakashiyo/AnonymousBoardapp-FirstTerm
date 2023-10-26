from django.db import models
import os
from boardapp.settings import MEDIA_ROOT

# Create your models here.
class Comment(models.Model):
    body = models.CharField(max_length=2000)    # 本文
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    file = models.FileField(upload_to='files', blank=True, null=True)
    password = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.file:
            file_path = self.file.path
            file_dir, file_name = os.path.split(file_path)
            new_file_name = f"{self.id}{os.path.splitext(file_name)[1]}"
            new_file_path = os.path.join(MEDIA_ROOT, new_file_name)
            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
            os.rename(file_path, new_file_path)
            self.file.name = os.path.relpath(new_file_path, MEDIA_ROOT)
            super().save(update_fields=['file'])

    class Meta:
        ordering = ['-updated_at'] # 降順ソート