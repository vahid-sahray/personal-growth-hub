from django.contrib import admin
from .models import Course, Module, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "order")
    prepopulated_fields = {"slug": ("title",)}
