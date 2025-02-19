from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_map_item import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem,
    )
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem,
    )


T = TypeVar("T", bound="GetV1EnterpriseSnapshotResponse200")


@_attrs_define
class GetV1EnterpriseSnapshotResponse200:
    """
    Attributes:
        device_snapshot_records (Union[Unset, list['GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem']]):
        device_snapshot_map (Union[Unset, list['GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem']]):
    """

    device_snapshot_records: Union[Unset, list["GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem"]] = UNSET
    device_snapshot_map: Union[Unset, list["GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_snapshot_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_snapshot_records, Unset):
            device_snapshot_records = []
            for device_snapshot_records_item_data in self.device_snapshot_records:
                device_snapshot_records_item = device_snapshot_records_item_data.to_dict()
                device_snapshot_records.append(device_snapshot_records_item)

        device_snapshot_map: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_snapshot_map, Unset):
            device_snapshot_map = []
            for device_snapshot_map_item_data in self.device_snapshot_map:
                device_snapshot_map_item = device_snapshot_map_item_data.to_dict()
                device_snapshot_map.append(device_snapshot_map_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_snapshot_records is not UNSET:
            field_dict["deviceSnapshotRecords"] = device_snapshot_records
        if device_snapshot_map is not UNSET:
            field_dict["deviceSnapshotMap"] = device_snapshot_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_map_item import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem,
        )
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem,
        )

        d = src_dict.copy()
        device_snapshot_records = []
        _device_snapshot_records = d.pop("deviceSnapshotRecords", UNSET)
        for device_snapshot_records_item_data in _device_snapshot_records or []:
            device_snapshot_records_item = GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItem.from_dict(
                device_snapshot_records_item_data
            )

            device_snapshot_records.append(device_snapshot_records_item)

        device_snapshot_map = []
        _device_snapshot_map = d.pop("deviceSnapshotMap", UNSET)
        for device_snapshot_map_item_data in _device_snapshot_map or []:
            device_snapshot_map_item = GetV1EnterpriseSnapshotResponse200DeviceSnapshotMapItem.from_dict(
                device_snapshot_map_item_data
            )

            device_snapshot_map.append(device_snapshot_map_item)

        get_v1_enterprise_snapshot_response_200 = cls(
            device_snapshot_records=device_snapshot_records,
            device_snapshot_map=device_snapshot_map,
        )

        get_v1_enterprise_snapshot_response_200.additional_properties = d
        return get_v1_enterprise_snapshot_response_200

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
