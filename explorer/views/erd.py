from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View

from explorer import app_settings
from explorer.forms import QueryForm
from explorer.models import MSG_FAILED_BLACKLIST, Query, QueryLog
from explorer.utils import (
    url_get_fullscreen, url_get_log_id, url_get_params, url_get_query_id, url_get_rows, url_get_show,
    InvalidExplorerConnectionException
)
from explorer.views.auth import PermissionRequiredMixin
from explorer.views.mixins import ExplorerContextMixin
from explorer.views.utils import query_viewmodel


class ERDMaskingView(PermissionRequiredMixin, ExplorerContextMixin, View):
    permission_required = "change_permission"

    def get(self, request):
        query = Query(title="ERD Masking")
        form = QueryForm(instance=query)
        return self.render(request, form=form)

    def post(self, request):
        form = QueryForm(request.POST)
        if form.is_valid():
            # Логика генерации ERD и маскирования данных
            pass
        return self.render(request, form=form)

    def render(self, request, form=None):
        return self.render_template(
            "explorer/erd_masking.html",
            {
                "title": "ERD Masking",
                "form": form
            }
        )
