from wagtail.snippets.models import register_snippet

from home.models import Employee
from home.views import EmployeeViewSet

from django.urls import path, reverse

from wagtail.admin.menu import MenuItem
from wagtail import hooks

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

register_snippet(Employee, viewset=EmployeeViewSet)


class BookAdmin(ModelAdmin):
    model = Employee
    menu_label = 'Список сотрудников'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('fio', 't' )
    list_filter = ('t',)
    search_fields = ('t', 'fio')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(BookAdmin)