from django.apps import AppConfig

from .utils.model import load_model_inference


class RequestsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "requests"
    ML_MODEL = load_model_inference("./model.pt")
