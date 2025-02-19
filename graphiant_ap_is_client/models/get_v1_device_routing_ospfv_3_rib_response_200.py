from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_3_rib_response_200_page_info import (
        GetV1DeviceRoutingOspfv3RibResponse200PageInfo,
    )
    from ..models.get_v1_device_routing_ospfv_3_rib_response_200_routes_item import (
        GetV1DeviceRoutingOspfv3RibResponse200RoutesItem,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv3RibResponse200")


@_attrs_define
class GetV1DeviceRoutingOspfv3RibResponse200:
    """
    Attributes:
        page_info (Union[Unset, GetV1DeviceRoutingOspfv3RibResponse200PageInfo]):
        routes (Union[Unset, list['GetV1DeviceRoutingOspfv3RibResponse200RoutesItem']]):
        token (Union[Unset, str]):  Example: xxxxxxxxx.
    """

    page_info: Union[Unset, "GetV1DeviceRoutingOspfv3RibResponse200PageInfo"] = UNSET
    routes: Union[Unset, list["GetV1DeviceRoutingOspfv3RibResponse200RoutesItem"]] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if routes is not UNSET:
            field_dict["routes"] = routes
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_3_rib_response_200_page_info import (
            GetV1DeviceRoutingOspfv3RibResponse200PageInfo,
        )
        from ..models.get_v1_device_routing_ospfv_3_rib_response_200_routes_item import (
            GetV1DeviceRoutingOspfv3RibResponse200RoutesItem,
        )

        d = src_dict.copy()
        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1DeviceRoutingOspfv3RibResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1DeviceRoutingOspfv3RibResponse200PageInfo.from_dict(_page_info)

        routes = []
        _routes = d.pop("routes", UNSET)
        for routes_item_data in _routes or []:
            routes_item = GetV1DeviceRoutingOspfv3RibResponse200RoutesItem.from_dict(routes_item_data)

            routes.append(routes_item)

        token = d.pop("token", UNSET)

        get_v1_device_routing_ospfv_3_rib_response_200 = cls(
            page_info=page_info,
            routes=routes,
            token=token,
        )

        get_v1_device_routing_ospfv_3_rib_response_200.additional_properties = d
        return get_v1_device_routing_ospfv_3_rib_response_200

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
