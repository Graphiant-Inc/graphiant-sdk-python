from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_traffic_policy_dpi_applications_item_value import (
        PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItemValue,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItem")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItem:
    """
    Attributes:
        key (Union[Unset, str]):  Example: TYPE_STRING.
        value (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItemValue]):
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItemValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_traffic_policy_dpi_applications_item_value import (
            PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItemValue,
        )

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItemValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PutV1DevicesDeviceIdConfigBodyEdgeTrafficPolicyDpiApplicationsItemValue.from_dict(_value)

        put_v1_devices_device_id_config_body_edge_traffic_policy_dpi_applications_item = cls(
            key=key,
            value=value,
        )

        put_v1_devices_device_id_config_body_edge_traffic_policy_dpi_applications_item.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_traffic_policy_dpi_applications_item

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
