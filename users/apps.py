from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        try:
            from django.contrib.admin.models import LogEntry
            from django.contrib.sessions.models import Session
            from model_history.models import History, HistoryLog
            from django.apps import apps
            models = apps.get_models('users')
            from users.models import User

            History.register(User, exclude=["password"])
            for model in models:
                if model not in [LogEntry, History, HistoryLog, Session, User]:
                    History.register(model)
        except Exception:
            pass
