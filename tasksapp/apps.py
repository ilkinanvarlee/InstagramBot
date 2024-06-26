from django.apps import AppConfig


class TasksappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasksapp'

    def ready(self):
        try:
            import tasksapp.tasks
        except ImportError:
            pass
