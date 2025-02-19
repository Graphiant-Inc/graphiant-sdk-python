from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_rib_vrf_default_exist_response_200_default_item import (
        GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingRibVrfDefaultExistResponse200")


@_attrs_define
class GetV1DeviceRoutingRibVrfDefaultExistResponse200:
    """
    Attributes:
        default (Union[Unset, list['GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem']]):
    """

    default: Union[Unset, list["GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.default, Unset):
            default = []
            for default_item_data in self.default:
                default_item = default_item_data.to_dict()
                default.append(default_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_rib_vrf_default_exist_response_200_default_item import (
            GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem,
        )

        d = src_dict.copy()
        default = []
        _default = d.pop("default", UNSET)
        for default_item_data in _default or []:
            default_item = GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem.from_dict(default_item_data)

            default.append(default_item)

        get_v1_device_routing_rib_vrf_default_exist_response_200 = cls(
            default=default,
        )

        get_v1_device_routing_rib_vrf_default_exist_response_200.additional_properties = d
        return get_v1_device_routing_rib_vrf_default_exist_response_200

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
