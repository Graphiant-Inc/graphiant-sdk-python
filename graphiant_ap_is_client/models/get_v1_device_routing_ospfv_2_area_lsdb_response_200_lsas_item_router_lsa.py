from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item import (
        GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsa")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsa:
    """
    Attributes:
        links (Union[Unset, list['GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem']]):
    """

    links: Union[Unset, list["GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item import (
            GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem,
        )

        d = src_dict.copy()
        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem.from_dict(
                links_item_data
            )

            links.append(links_item)

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa = cls(
            links=links,
        )

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa

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
