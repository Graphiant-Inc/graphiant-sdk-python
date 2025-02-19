from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_snapshot_response_200_first_snapshot import GetV1DeviceSnapshotResponse200FirstSnapshot
    from ..models.get_v1_device_snapshot_response_200_second_snapshot import (
        GetV1DeviceSnapshotResponse200SecondSnapshot,
    )
    from ..models.get_v1_device_snapshot_response_200_third_snapshot import GetV1DeviceSnapshotResponse200ThirdSnapshot


T = TypeVar("T", bound="GetV1DeviceSnapshotResponse200")


@_attrs_define
class GetV1DeviceSnapshotResponse200:
    """
    Attributes:
        first_snapshot (Union[Unset, GetV1DeviceSnapshotResponse200FirstSnapshot]):
        second_snapshot (Union[Unset, GetV1DeviceSnapshotResponse200SecondSnapshot]):
        third_snapshot (Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshot]):
    """

    first_snapshot: Union[Unset, "GetV1DeviceSnapshotResponse200FirstSnapshot"] = UNSET
    second_snapshot: Union[Unset, "GetV1DeviceSnapshotResponse200SecondSnapshot"] = UNSET
    third_snapshot: Union[Unset, "GetV1DeviceSnapshotResponse200ThirdSnapshot"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_snapshot, Unset):
            first_snapshot = self.first_snapshot.to_dict()

        second_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.second_snapshot, Unset):
            second_snapshot = self.second_snapshot.to_dict()

        third_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.third_snapshot, Unset):
            third_snapshot = self.third_snapshot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_snapshot is not UNSET:
            field_dict["firstSnapshot"] = first_snapshot
        if second_snapshot is not UNSET:
            field_dict["secondSnapshot"] = second_snapshot
        if third_snapshot is not UNSET:
            field_dict["thirdSnapshot"] = third_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_snapshot_response_200_first_snapshot import (
            GetV1DeviceSnapshotResponse200FirstSnapshot,
        )
        from ..models.get_v1_device_snapshot_response_200_second_snapshot import (
            GetV1DeviceSnapshotResponse200SecondSnapshot,
        )
        from ..models.get_v1_device_snapshot_response_200_third_snapshot import (
            GetV1DeviceSnapshotResponse200ThirdSnapshot,
        )

        d = src_dict.copy()
        _first_snapshot = d.pop("firstSnapshot", UNSET)
        first_snapshot: Union[Unset, GetV1DeviceSnapshotResponse200FirstSnapshot]
        if isinstance(_first_snapshot, Unset):
            first_snapshot = UNSET
        else:
            first_snapshot = GetV1DeviceSnapshotResponse200FirstSnapshot.from_dict(_first_snapshot)

        _second_snapshot = d.pop("secondSnapshot", UNSET)
        second_snapshot: Union[Unset, GetV1DeviceSnapshotResponse200SecondSnapshot]
        if isinstance(_second_snapshot, Unset):
            second_snapshot = UNSET
        else:
            second_snapshot = GetV1DeviceSnapshotResponse200SecondSnapshot.from_dict(_second_snapshot)

        _third_snapshot = d.pop("thirdSnapshot", UNSET)
        third_snapshot: Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshot]
        if isinstance(_third_snapshot, Unset):
            third_snapshot = UNSET
        else:
            third_snapshot = GetV1DeviceSnapshotResponse200ThirdSnapshot.from_dict(_third_snapshot)

        get_v1_device_snapshot_response_200 = cls(
            first_snapshot=first_snapshot,
            second_snapshot=second_snapshot,
            third_snapshot=third_snapshot,
        )

        get_v1_device_snapshot_response_200.additional_properties = d
        return get_v1_device_snapshot_response_200

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
