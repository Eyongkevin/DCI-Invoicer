from typing import Dict, List

from django import template

register = template.Library()


@register.inclusion_tag("task_list.html")
def task_list(task: str) -> Dict[str, List[str]]:
    tasks: List[str] = task.split("\n")
    tasks = [value.strip("-").strip() for value in tasks]
    return {"tasks": tasks}
