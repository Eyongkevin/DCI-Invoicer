from typing import Dict, NoReturn, Tuple, Union

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView

from apps.core.exceptions import (
    UserLoginFailedEx,
    UserMismatchPasswordsEx,
    UserMissingCpasswordEx,
    UserNonDCIFreelancerEmailEx,
)
from apps.core.permissions import OnlyAdminAndSuperuserPermission, UserPermission
from apps.user.models import User

from .permissions import OnlySuperuserCreateSuperuserPermission
from .serializers import LoginSerializer, RegistrationSerializer

# Create your views here.


class LoginViewSet(ViewSet):
    http_method_names: Tuple[str] = ("post",)
    serializer_classes: TokenObtainPairSerializer = LoginSerializer
    permission_classes: Tuple[BasePermission] = (AllowAny,)

    def create(self, request, *args, **kwargs) -> Union[Response, NoReturn]:
        serializer: LoginSerializer = self.serializer_classes(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as err:
            raise InvalidToken(err.args[0]) from err
        except AuthenticationFailed as err:
            raise UserLoginFailedEx() from err
        return Response(
            serializer.validated_data,
            status=status.HTTP_201_CREATED,
        )


class RegisterViewSet(ViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = (
        UserPermission,
        OnlyAdminAndSuperuserPermission,
        OnlySuperuserCreateSuperuserPermission,
    )
    http_method_names = ("post",)

    def create(self, request, *args, **kwargs) -> Union[Response, NoReturn]:
        password: str = request.data.get("password")
        cpassword: str = request.data.get("cpassword")

        try:
            del request.data["cpassword"]
        except KeyError as err:
            raise UserMissingCpasswordEx()

        if password != cpassword:
            raise UserMismatchPasswordsEx()

        serializer: RegistrationSerializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except UserNonDCIFreelancerEmailEx as err:
            raise UserNonDCIFreelancerEmailEx() from err
        except Exception as err:
            message: str = err.args[0]
            message.update({"code": "field_validation_error"})
            raise ValidationError(message) from err

        user: User = serializer.save()
        res: Dict[str, str] = {"username": user.username, "password": password}

        return Response(res, status=status.HTTP_201_CREATED)


class RefreshViewSet(ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ("post",)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as err:
            raise InvalidToken(err.args[0]) from err
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
