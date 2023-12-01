from django import template

register = template.Library()


@register.filter
def remove_dash(value: str) -> str:
    return value.strip("-").strip()
