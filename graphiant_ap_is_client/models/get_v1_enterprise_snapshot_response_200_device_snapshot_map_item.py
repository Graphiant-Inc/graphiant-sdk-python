from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue,
    )


T = TypeVar("T", bound="GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem")


@_attrs_define
class GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem:
    """
    Attributes:
        key (Union[Unset, str]):  Example: TYPE_INT64.
        value (Union[Unset, GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue]):
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, "GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue"] = UNSET
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
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_map_item_value import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue,
        )

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItemValue.from_dict(_value)

        get_v1_enterprise_snapshot_response_200_device_snapshot_map_item = cls(
            key=key,
            value=value,
        )

        get_v1_enterprise_snapshot_response_200_device_snapshot_map_item.additional_properties = d
        return get_v1_enterprise_snapshot_response_200_device_snapshot_map_item

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
