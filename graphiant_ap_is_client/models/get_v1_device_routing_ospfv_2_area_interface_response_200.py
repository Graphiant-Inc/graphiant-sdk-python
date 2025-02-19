from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_2_area_interface_response_200_interfaces_item import (
        GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem,
    )
    from ..models.get_v1_device_routing_ospfv_2_area_interface_response_200_page_info import (
        GetV1DeviceRoutingOspfv2AreaInterfaceResponse200PageInfo,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaInterfaceResponse200")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaInterfaceResponse200:
    """
    Attributes:
        interfaces (Union[Unset, list['GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem']]):
        page_info (Union[Unset, GetV1DeviceRoutingOspfv2AreaInterfaceResponse200PageInfo]):
        token (Union[Unset, str]):  Example: xxxxxxxxx.
    """

    interfaces: Union[Unset, list["GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem"]] = UNSET
    page_info: Union[Unset, "GetV1DeviceRoutingOspfv2AreaInterfaceResponse200PageInfo"] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_2_area_interface_response_200_interfaces_item import (
            GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem,
        )
        from ..models.get_v1_device_routing_ospfv_2_area_interface_response_200_page_info import (
            GetV1DeviceRoutingOspfv2AreaInterfaceResponse200PageInfo,
        )

        d = src_dict.copy()
        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem.from_dict(
                interfaces_item_data
            )

            interfaces.append(interfaces_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1DeviceRoutingOspfv2AreaInterfaceResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1DeviceRoutingOspfv2AreaInterfaceResponse200PageInfo.from_dict(_page_info)

        token = d.pop("token", UNSET)

        get_v1_device_routing_ospfv_2_area_interface_response_200 = cls(
            interfaces=interfaces,
            page_info=page_info,
            token=token,
        )

        get_v1_device_routing_ospfv_2_area_interface_response_200.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_interface_response_200

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
