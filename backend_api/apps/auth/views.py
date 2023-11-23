from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from .serializers import LoginSerializer

# Create your views here.


class LoginViewSet(ViewSet):
    http_method_names = ("post",)
    serializer_classes = LoginSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_classes(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as err:
            raise InvalidToken(err.args[0]) from err
        except AuthenticationFailed as err:
            raise AuthenticationFailed(
                detail="Incorrect username or password",
                code=status.HTTP_401_UNAUTHORIZED,
            ) from err
        return Response(
            serializer.validated_data,
            status=status.HTTP_201_CREATED,
        )
