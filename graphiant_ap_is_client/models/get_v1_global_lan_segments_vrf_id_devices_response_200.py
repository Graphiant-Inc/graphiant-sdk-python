from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_lan_segments_vrf_id_devices_response_200_entries_item import (
        GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem,
    )


T = TypeVar("T", bound="GetV1GlobalLanSegmentsVrfIdDevicesResponse200")


@_attrs_define
class GetV1GlobalLanSegmentsVrfIdDevicesResponse200:
    """
    Attributes:
        entries (Union[Unset, list['GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem']]):
        status (Union[Unset, str]):  Example: TYPE_STRING.
    """

    entries: Union[Unset, list["GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_lan_segments_vrf_id_devices_response_200_entries_item import (
            GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem,
        )

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = GetV1GlobalLanSegmentsVrfIdDevicesResponse200EntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        status = d.pop("status", UNSET)

        get_v1_global_lan_segments_vrf_id_devices_response_200 = cls(
            entries=entries,
            status=status,
        )

        get_v1_global_lan_segments_vrf_id_devices_response_200.additional_properties = d
        return get_v1_global_lan_segments_vrf_id_devices_response_200

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
