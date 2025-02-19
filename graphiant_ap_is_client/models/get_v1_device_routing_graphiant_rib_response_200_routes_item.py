from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_graphiant_rib_response_200_routes_item_path_item import (
        GetV1DeviceRoutingGraphiantRibResponse200RoutesItemPathItem,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingGraphiantRibResponse200RoutesItem")


@_attrs_define
class GetV1DeviceRoutingGraphiantRibResponse200RoutesItem:
    """
    Attributes:
        ip_prefix (Union[Unset, str]):  Example: 131.1.0.0/16.
        path (Union[Unset, list['GetV1DeviceRoutingGraphiantRibResponse200RoutesItemPathItem']]):
    """

    ip_prefix: Union[Unset, str] = UNSET
    path: Union[Unset, list["GetV1DeviceRoutingGraphiantRibResponse200RoutesItemPathItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_prefix = self.ip_prefix

        path: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item = path_item_data.to_dict()
                path.append(path_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip_prefix is not UNSET:
            field_dict["ipPrefix"] = ip_prefix
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_graphiant_rib_response_200_routes_item_path_item import (
            GetV1DeviceRoutingGraphiantRibResponse200RoutesItemPathItem,
        )

        d = src_dict.copy()
        ip_prefix = d.pop("ipPrefix", UNSET)

        path = []
        _path = d.pop("path", UNSET)
        for path_item_data in _path or []:
            path_item = GetV1DeviceRoutingGraphiantRibResponse200RoutesItemPathItem.from_dict(path_item_data)

            path.append(path_item)

        get_v1_device_routing_graphiant_rib_response_200_routes_item = cls(
            ip_prefix=ip_prefix,
            path=path,
        )

        get_v1_device_routing_graphiant_rib_response_200_routes_item.additional_properties = d
        return get_v1_device_routing_graphiant_rib_response_200_routes_item

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
