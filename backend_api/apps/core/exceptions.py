from typing import Dict, Literal

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, ValidationError


class UserLoginFailedEx(AuthenticationFailed):
    def __init__(self) -> None:
        self.detail: Dict[str, str] = {
            "detail": "Incorrect username or password",
            "code": "credential_incorrect",
        }
        self.code: Literal[401] = status.HTTP_401_UNAUTHORIZED
        super().__init__(self.detail, self.code)


class UserMismatchPasswordsEx(ValidationError):
    def __init__(self) -> None:
        self.detail: Dict[str, str] = {
            "detail": "password and cpassword must match",
            "code": "mismatch_passwords",
        }
        self.code: Literal[400] = status.HTTP_400_BAD_REQUEST
        super().__init__(self.detail, self.code)


class UserMissingCpasswordEx(ValidationError):
    def __init__(self) -> None:
        self.detail: Dict[str, str] = {
            "detail": "cpassword must be provided",
            "code": "missing_cpassword",
        }
        self.code: Literal[400] = status.HTTP_400_BAD_REQUEST
        super().__init__(self.detail, self.code)


class UserNonDCIFreelancerEmailEx(ValidationError):
    def __init__(self) -> None:
        self.detail: Dict[str, str] = {
            "detail": "Email should be a DCI freelancer email",
            "code": "non_dci_freelancer_email",
        }
        self.code: Literal[400] = status.HTTP_400_BAD_REQUEST
        super().__init__(self.detail, self.code)
