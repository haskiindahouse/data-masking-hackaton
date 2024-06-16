from io import BytesIO
from typing import Iterable, Optional

from django.core.exceptions import ImproperlyConfigured

from explorer import app_settings


if app_settings.EXPLORER_CHARTS_ENABLED:
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        from matplotlib.figure import Figure
    except ImportError as err:
        raise ImproperlyConfigured(
            "If `EXPLORER_CHARTS_ENABLED` is enabled, `matplotlib` and `seaborn` must be installed."
        ) from err

from .models import QueryResult


def get_pie_chart(result: QueryResult) -> Optional[str]:
    if len(result.data) < 1 or len(result.data[0]) < 2:
        return None
    not_none_rows = [row for row in result.data if row[0] is not None and row[1] is not None]
    labels = [row[0] for row in not_none_rows]
    values = [row[1] for row in not_none_rows]
    if not is_numeric(values):
        return None
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    ax.pie(values, labels=labels)
    return get_svg(fig)


def get_line_chart(result: QueryResult) -> Optional[str]:
    if len(result.data) < 1:
        return None
    numeric_columns = [
        c for c in range(1, len(result.data[0]))
        if all([isinstance(col[c], (int, float)) or col[c] is None for col in result.data])
    ]
    if len(numeric_columns) < 1:
        return None
    labels = [row[0] for row in result.data]
    fig, ax = plt.subplots(figsize=(10, 3.8))
    for col_num in numeric_columns:
        sns.lineplot(ax=ax,
                     x=labels,
                     y=[row[col_num] for row in result.data],
                     label=result.headers[col_num])
    ax.set_xlabel(result.headers[0])
    # Rotate x-axis labels by 20 degrees to reduce overlap
    for label in ax.get_xticklabels():
        label.set_rotation(20)
        label.set_ha("right")
    return get_svg(fig)


def get_svg(fig: "Figure") -> str:
    buffer = BytesIO()
    fig.savefig(buffer, format="svg")
    buffer.seek(0)
    graph = buffer.getvalue().decode("utf-8")
    buffer.close()
    return graph


def is_numeric(column: Iterable) -> bool:
    return all([isinstance(value, (int, float)) or value is None for value in column])
