from django.contrib import admin

from appname.models import Example


class ExampleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Example, ExampleAdmin)
