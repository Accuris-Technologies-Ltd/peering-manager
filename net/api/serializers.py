from net.enums import ConnectionStatus
from net.models import Connection
from peering.api.nested_serializers import (
    NestedInternetExchangeSerializer,
    NestedRouterSerializer,
)
from peering_manager.api.fields import ChoiceField
from peering_manager.api.serializers import PeeringManagerModelSerializer

from .nested_serializers import *

__all__ = ("ConnectionSerializer", "NestedConnectionSerializer")


class ConnectionSerializer(PeeringManagerModelSerializer):
    name = serializers.CharField(read_only=True)
    status = ChoiceField(required=False, choices=ConnectionStatus)
    internet_exchange_point = NestedInternetExchangeSerializer(allow_null=True)
    router = NestedRouterSerializer(allow_null=True)

    class Meta:
        model = Connection
        fields = [
            "id",
            "display",
            "name",
            "peeringdb_netixlan",
            "status",
            "vlan",
            "mac_address",
            "ipv6_address",
            "ipv4_address",
            "internet_exchange_point",
            "router",
            "interface",
            "description",
            "local_context_data",
            "comments",
            "tags",
        ]
