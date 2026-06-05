from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_ap = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="module")

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")

    title = models.CharField(max_length=255)
    slug = models.SlugField()

    summary = models.TextField(max_length=255)
    
    content_path = models.CharField(max_length=255, blank=True)

    order = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

















