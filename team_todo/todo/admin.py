from django.contrib import admin
from .models import Board, Task, TaskComment

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_public', 'created_at')
    search_fields = ('name', 'description', 'owner__username')
    list_filter = ('is_public', 'created_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'board', 'status', 'created_by', 'created_at')
    search_fields = ('title', 'description', 'created_by__username', 'board__name')
    list_filter = ('status', 'created_at')

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'created_at')
    search_fields = ('task__title', 'author__username', 'text')
    list_filter = ('created_at',)
