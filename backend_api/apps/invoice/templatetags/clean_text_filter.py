from django import template

register = template.Library()


@register.filter
def remove_dash(value: str) -> str:
    return value.strip("-").strip()


@register.filter
def is_nested(value: str) -> bool:
    return value.startswith("-")
