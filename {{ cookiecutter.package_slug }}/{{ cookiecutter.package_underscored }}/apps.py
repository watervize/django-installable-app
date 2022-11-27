from django.apps import AppConfig


class {{ cookiecutter.package_name|camelcase_extension }}AppConfig(AppConfig):
    name = "{{ cookiecutter.package_slug }}"
    verbose_name = "{{ cookiecutter.package_name }}"

    def ready(self):
        pass

