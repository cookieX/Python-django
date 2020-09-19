import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import (
    UserSignUpSerializer,
    ProfileInfoSerializer,
    UserProfileSerializer,
    FollowSerializer,
    AllUserListSerializer,
    ChangePasswordSerializer,
)
import django_filters.filters
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

User = get_user_model()


class Userilter(django_filters.FilterSet):
    result = django_filters.CharFilter(
        method="my_custom_filter", label="Username Email, name"
    )

    class Meta:
        model = User
        fields = ["username"]

    def my_custom_filter(self, queryset, name, value):
        return User.objects.filter(
            Q(username__icontains=value)
            | Q(fullname__icontains=value)
            | Q(email__icontains=value)
        )


class UpdatePassword(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowersLikersPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 5000


class UserSignUpView(generics.CreateAPIView):
    """View For User Registration"""

    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    def get(self, request):
        return Response(
            {"minPasswordChars": 8, "help_text": "RET-ZURICHTEAM register API",}
        )

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(
                {"detail": "All The Fields Are Required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            serializer = UserSignUpSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileInfoSerializer

    def get_object(self):
        return self.request.user


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = AllUserListSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = Userilter


class UserProfileView(generics.RetrieveAPIView):
    lookup_field = "username"
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)


class FollowUserView(APIView):
    def get(self, request, format=None, username=None):
        to_user = get_user_model().objects.get(username=username)
        from_user = self.request.user
        follow = None
        if from_user.is_authenticated:
            if from_user != to_user:
                if from_user in to_user.followers.all():
                    follow = False
                    from_user.following.remove(to_user)
                    to_user.followers.remove(from_user)
                else:
                    follow = True
                    from_user.following.add(to_user)
                    to_user.followers.add(from_user)
        data = {"follow": follow}
        return Response(data)


class GetFollowersView(generics.ListAPIView):
    serializer_class = FollowSerializer
    pagination_class = FollowersLikersPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        username = self.kwargs["username"]
        queryset = get_user_model().objects.get(username=username).followers.all()
        return queryset


class GetFollowingView(generics.ListAPIView):
    serializer_class = FollowSerializer
    pagination_class = FollowersLikersPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        username = self.kwargs["username"]
        queryset = get_user_model().objects.get(username=username).following.all()
        return queryset
