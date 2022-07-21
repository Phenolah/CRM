from django.apps import AppConfig
 

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

class FooConfig(AppConfig):
    name = 'full.python.path.to.your.app.foo'
    label = 'my.foo'  

