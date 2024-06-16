from django import template

register = template.Library()

@register.filter(name='mask_sensitive_data')
def mask_sensitive_data(value):
    # Реализация фильтра для маскирования чувствительных данных
    # Пример: замена всех символов на '*'
    if isinstance(value, str):
        return '*' * len(value)
    return value
