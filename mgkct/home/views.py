from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.views.snippets import SnippetViewSet

from home.models import Employee


class EmployeeViewSet(SnippetViewSet):
    list_display = ["fio", "t", UpdatedAtColumn()]