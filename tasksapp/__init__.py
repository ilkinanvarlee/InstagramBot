from . celery import app as celery_app
default_app_config = 'tasksapp.apps.TasksappConfig'

__all__ = ('celery_app',)
