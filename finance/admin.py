from django.contrib import admin
from django.apps import apps


finance_models = apps.get_app_config('finance').get_models()

for model in finance_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
