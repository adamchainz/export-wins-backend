from rest_framework.decorators import list_route
from rest_framework.filters import DjangoFilterBackend, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .. import notifications
from ..filters import CustomerResponseFilterSet
from ..models import Win, Breakdown, Advisor, CustomerResponse, Notification
from ..serializers import (
    WinSerializer, LimitedWinSerializer, BreakdownSerializer,
    AdvisorSerializer, CustomerResponseSerializer, DetailWinSerializer
)
from alice.views import AliceMixin


class StandardPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page-size"


class BigPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = "page-size"


class WinViewSet(AliceMixin, ModelViewSet):
    """ For querying Wins and adding/editing """

    model = Win
    queryset = Win.objects.all()
    serializer_class = WinSerializer
    pagination_class = BigPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('id', 'user__id')
    ordering_fields = ("pk",)
    http_method_names = ("get", "post", "put", "patch")

    def _notify_if_complete(self, instance):
        """ If the form is marked 'complete', email customer for response """

        if not instance.complete:
            return

        notification_sent = Notification.objects.filter(
            win=instance,
            type=Notification.TYPE_CUSTOMER,
        ).count()

        if notification_sent:
            return

        notification = Notification(
            win=instance,
            user=self.request.user,
            recipient=instance.customer_email_address,
            type=Notification.TYPE_CUSTOMER,
        )
        notification.save()
        notifications.send_customer_email(instance)
        notifications.send_other_officers_email(instance)

    def perform_create(self, serializer):
        instance = serializer.save()
        self._notify_if_complete(instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        self._notify_if_complete(instance)


class LimitedWinViewSet(WinViewSet):
    """ Limited view for customer response """

    serializer_class = LimitedWinSerializer
    permission_classes = (AllowAny,)
    http_method_names = ("get",)

    def get_queryset(self):

        # We only allow for specific wins to be queried here
        if "pk" not in self.kwargs:
            return WinViewSet.get_queryset(self).none()

        # Limit records to wins that have not already been confirmed
        return WinViewSet.get_queryset(self).filter(
            pk=self.kwargs["pk"],
            confirmation__isnull=True
        )


class DetailsWinViewSet(WinViewSet):
    """ Provides additional Win data for details view """

    serializer_class = DetailWinSerializer
    permission_classes = (AllowAny,)
    http_method_names = ("get",)


class ConfirmationViewSet(AliceMixin, ModelViewSet):

    model = CustomerResponse
    queryset = CustomerResponse.objects.all()
    serializer_class = CustomerResponseSerializer
    pagination_class = StandardPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = CustomerResponseFilterSet
    ordering_fields = ("pk",)
    http_method_names = ("get", "post")

    def perform_create(self, serializer):
        """ Send officer notification when customer responds """

        instance = serializer.save()
        notifications.send_officer_notification_of_customer_response(instance)

        # some customer responses were sent manually in early days of the
        # system, so their wins may not be marked complete
        win = instance.win
        if not win.complete:
            win.complete = True
            win.save()

        return instance


class BreakdownViewSet(AliceMixin, ModelViewSet):

    model = Breakdown
    queryset = Breakdown.objects.all()
    serializer_class = BreakdownSerializer
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('win__id',)
    ordering_fields = ("pk",)
    http_method_names = ("get", "post", "patch", "put", "delete")


class AdvisorViewSet(AliceMixin, ModelViewSet):

    model = Advisor
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('win__id',)
    ordering_fields = ("pk",)
    http_method_names = ("get", "post", "patch", "put", "delete")
