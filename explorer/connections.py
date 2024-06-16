from django.db import connections as djcs
from django.db import transaction, DEFAULT_DB_ALIAS

from explorer.ee.db_connections.utils import create_django_style_connection
from explorer import app_settings
from explorer.models import DatabaseConnection


def new_get_connection(using=None):
    if using is None:
        using = DEFAULT_DB_ALIAS
    if using in djcs:
        return djcs[using]
    return create_django_style_connection(DatabaseConnection.objects.get(alias=using))


transaction.get_connection = new_get_connection

class ExplorerConnections(dict):

    def __getitem__(self, item):
        if item in djcs:
            return djcs[item]
        else:
            return create_django_style_connection(DatabaseConnection.objects.get(alias=item))


def connections():
    _connections = [c for c in djcs if c in app_settings.EXPLORER_CONNECTIONS.values()]
    db_connections = DatabaseConnection.objects.all()
    _connections += [c.alias for c in db_connections]
    return ExplorerConnections(zip(_connections, _connections))


