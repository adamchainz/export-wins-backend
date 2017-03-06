import json

from django.contrib.auth import login
from django.http import HttpResponse

from rest_framework import parsers, renderers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoggingAuthTokenSerializer


class LoginView(APIView):

    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = LoggingAuthTokenSerializer
    http_method_names = ("post")

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get authenticated user (will raise exception otherwise)
        user = serializer.validated_data['user']

        # create session for the user
        login(request, user)

        return Response({
            'id': user.pk,
            'email': user.email,
            'is_staff': user.is_staff,
        })


class IsLoggedIn(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ("get",)

    def get(self, request):
        return HttpResponse(json.dumps(bool(request.user.is_authenticated())))
