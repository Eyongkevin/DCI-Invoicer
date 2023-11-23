from enum import Enum


class UserRoleEnum(Enum):
    user: str = "US"
    admin: str = "AD"
    superuser: str = "SU"
