from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_3_area_interfaceid_response_200_page_info import (
        GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200PageInfo,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200")


@_attrs_define
class GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200:
    """
    Attributes:
        interfaces (Union[Unset, list[str]]):  Example: ['ToATT, Ethernet1/0'].
        page_info (Union[Unset, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200PageInfo]):
        token (Union[Unset, str]):  Example: xxxxxxxxx.
    """

    interfaces: Union[Unset, list[str]] = UNSET
    page_info: Union[Unset, "GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200PageInfo"] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: Union[Unset, list[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

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
        from ..models.get_v1_device_routing_ospfv_3_area_interfaceid_response_200_page_info import (
            GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200PageInfo,
        )

        d = src_dict.copy()
        interfaces = cast(list[str], d.pop("interfaces", UNSET))

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1DeviceRoutingOspfv3AreaInterfaceidResponse200PageInfo.from_dict(_page_info)

        token = d.pop("token", UNSET)

        get_v1_device_routing_ospfv_3_area_interfaceid_response_200 = cls(
            interfaces=interfaces,
            page_info=page_info,
            token=token,
        )

        get_v1_device_routing_ospfv_3_area_interfaceid_response_200.additional_properties = d
        return get_v1_device_routing_ospfv_3_area_interfaceid_response_200

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
