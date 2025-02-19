from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_asexternal_lsa import (
        GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemAsexternalLsa,
    )
    from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_network_lsa import (
        GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemNetworkLsa,
    )
    from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_router_lsa import (
        GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemRouterLsa,
    )
    from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_summary_lsa import (
        GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemSummaryLsa,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2LsdbResponse200LsasItem")


@_attrs_define
class GetV1DeviceRoutingOspfv2LsdbResponse200LsasItem:
    """
    Attributes:
        advertising_router (Union[Unset, str]):  Example: 172.121.12.34.
        age (Union[Unset, str]):  Example: 3242342.
        asexternal_lsa (Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemAsexternalLsa]):
        checksum (Union[Unset, str]):  Example: 2343232.
        length (Union[Unset, str]):  Example: 123132.
        link_id (Union[Unset, str]):  Example: 143.12.1.5.
        network_lsa (Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemNetworkLsa]):
        router_lsa (Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemRouterLsa]):
        sequence_number (Union[Unset, str]):  Example: 2147483649.
        summary_lsa (Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemSummaryLsa]):
        type_ (Union[Unset, str]):  Example: Router.
    """

    advertising_router: Union[Unset, str] = UNSET
    age: Union[Unset, str] = UNSET
    asexternal_lsa: Union[Unset, "GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemAsexternalLsa"] = UNSET
    checksum: Union[Unset, str] = UNSET
    length: Union[Unset, str] = UNSET
    link_id: Union[Unset, str] = UNSET
    network_lsa: Union[Unset, "GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemNetworkLsa"] = UNSET
    router_lsa: Union[Unset, "GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemRouterLsa"] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    summary_lsa: Union[Unset, "GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemSummaryLsa"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advertising_router = self.advertising_router

        age = self.age

        asexternal_lsa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.asexternal_lsa, Unset):
            asexternal_lsa = self.asexternal_lsa.to_dict()

        checksum = self.checksum

        length = self.length

        link_id = self.link_id

        network_lsa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network_lsa, Unset):
            network_lsa = self.network_lsa.to_dict()

        router_lsa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.router_lsa, Unset):
            router_lsa = self.router_lsa.to_dict()

        sequence_number = self.sequence_number

        summary_lsa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary_lsa, Unset):
            summary_lsa = self.summary_lsa.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advertising_router is not UNSET:
            field_dict["advertisingRouter"] = advertising_router
        if age is not UNSET:
            field_dict["age"] = age
        if asexternal_lsa is not UNSET:
            field_dict["asexternalLsa"] = asexternal_lsa
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if length is not UNSET:
            field_dict["length"] = length
        if link_id is not UNSET:
            field_dict["linkId"] = link_id
        if network_lsa is not UNSET:
            field_dict["networkLsa"] = network_lsa
        if router_lsa is not UNSET:
            field_dict["routerLsa"] = router_lsa
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if summary_lsa is not UNSET:
            field_dict["summaryLsa"] = summary_lsa
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_asexternal_lsa import (
            GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemAsexternalLsa,
        )
        from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_network_lsa import (
            GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemNetworkLsa,
        )
        from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_router_lsa import (
            GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemRouterLsa,
        )
        from ..models.get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item_summary_lsa import (
            GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemSummaryLsa,
        )

        d = src_dict.copy()
        advertising_router = d.pop("advertisingRouter", UNSET)

        age = d.pop("age", UNSET)

        _asexternal_lsa = d.pop("asexternalLsa", UNSET)
        asexternal_lsa: Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemAsexternalLsa]
        if isinstance(_asexternal_lsa, Unset):
            asexternal_lsa = UNSET
        else:
            asexternal_lsa = GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemAsexternalLsa.from_dict(_asexternal_lsa)

        checksum = d.pop("checksum", UNSET)

        length = d.pop("length", UNSET)

        link_id = d.pop("linkId", UNSET)

        _network_lsa = d.pop("networkLsa", UNSET)
        network_lsa: Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemNetworkLsa]
        if isinstance(_network_lsa, Unset):
            network_lsa = UNSET
        else:
            network_lsa = GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemNetworkLsa.from_dict(_network_lsa)

        _router_lsa = d.pop("routerLsa", UNSET)
        router_lsa: Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemRouterLsa]
        if isinstance(_router_lsa, Unset):
            router_lsa = UNSET
        else:
            router_lsa = GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemRouterLsa.from_dict(_router_lsa)

        sequence_number = d.pop("sequenceNumber", UNSET)

        _summary_lsa = d.pop("summaryLsa", UNSET)
        summary_lsa: Union[Unset, GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemSummaryLsa]
        if isinstance(_summary_lsa, Unset):
            summary_lsa = UNSET
        else:
            summary_lsa = GetV1DeviceRoutingOspfv2LsdbResponse200LsasItemSummaryLsa.from_dict(_summary_lsa)

        type_ = d.pop("type", UNSET)

        get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item = cls(
            advertising_router=advertising_router,
            age=age,
            asexternal_lsa=asexternal_lsa,
            checksum=checksum,
            length=length,
            link_id=link_id,
            network_lsa=network_lsa,
            router_lsa=router_lsa,
            sequence_number=sequence_number,
            summary_lsa=summary_lsa,
            type_=type_,
        )

        get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item.additional_properties = d
        return get_v1_device_routing_ospfv_2_lsdb_response_200_lsas_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
