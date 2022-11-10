from rest_framework import status, viewsets  # noqa
from rest_framework.response import Response  # noqa
from rest_framework.permissions import IsAuthenticated, AllowAny  # noqa

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # user name
        full_name = f"{user.first_name if user.first_name else ''}"
        full_name += f"{user.last_name if user.last_name else ''}"

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': full_name
        })


class LogoutApiView(APIView):
    def post(self, request, format=None):
        # simply delete the token to force a login
        print(request.user)
        user_id = request.data.get('user_id', None)
        if user_id is None:
            user = User.objects.get(user_id=user_id).first()
            user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)


class VideoLikeDislikeUsersAPIView(APIView):
    """ user detail and update """
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        user_ids = request.data.get('user_ids', None)
        users = User.objects.filter(pk__in=user_ids)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
