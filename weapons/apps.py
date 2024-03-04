from django.apps import AppConfig

from .utils.model import load_model_inference


class WeaponsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "weapons"
    ML_MODEL = load_model_inference("./model.pt")
