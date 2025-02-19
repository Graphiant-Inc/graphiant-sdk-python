from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_nat_entries_device_id_response_200_nat_entries_item import (
        GetV1NatEntriesDeviceIdResponse200NatEntriesItem,
    )
    from ..models.get_v1_nat_entries_device_id_response_200_page_info import GetV1NatEntriesDeviceIdResponse200PageInfo
    from ..models.get_v1_nat_entries_device_id_response_200_ts import GetV1NatEntriesDeviceIdResponse200Ts


T = TypeVar("T", bound="GetV1NatEntriesDeviceIdResponse200")


@_attrs_define
class GetV1NatEntriesDeviceIdResponse200:
    """
    Attributes:
        nat_entries (Union[Unset, list['GetV1NatEntriesDeviceIdResponse200NatEntriesItem']]):
        page_info (Union[Unset, GetV1NatEntriesDeviceIdResponse200PageInfo]):
        ts (Union[Unset, GetV1NatEntriesDeviceIdResponse200Ts]):
    """

    nat_entries: Union[Unset, list["GetV1NatEntriesDeviceIdResponse200NatEntriesItem"]] = UNSET
    page_info: Union[Unset, "GetV1NatEntriesDeviceIdResponse200PageInfo"] = UNSET
    ts: Union[Unset, "GetV1NatEntriesDeviceIdResponse200Ts"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nat_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nat_entries, Unset):
            nat_entries = []
            for nat_entries_item_data in self.nat_entries:
                nat_entries_item = nat_entries_item_data.to_dict()
                nat_entries.append(nat_entries_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nat_entries is not UNSET:
            field_dict["natEntries"] = nat_entries
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_nat_entries_device_id_response_200_nat_entries_item import (
            GetV1NatEntriesDeviceIdResponse200NatEntriesItem,
        )
        from ..models.get_v1_nat_entries_device_id_response_200_page_info import (
            GetV1NatEntriesDeviceIdResponse200PageInfo,
        )
        from ..models.get_v1_nat_entries_device_id_response_200_ts import GetV1NatEntriesDeviceIdResponse200Ts

        d = src_dict.copy()
        nat_entries = []
        _nat_entries = d.pop("natEntries", UNSET)
        for nat_entries_item_data in _nat_entries or []:
            nat_entries_item = GetV1NatEntriesDeviceIdResponse200NatEntriesItem.from_dict(nat_entries_item_data)

            nat_entries.append(nat_entries_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1NatEntriesDeviceIdResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1NatEntriesDeviceIdResponse200PageInfo.from_dict(_page_info)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, GetV1NatEntriesDeviceIdResponse200Ts]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = GetV1NatEntriesDeviceIdResponse200Ts.from_dict(_ts)

        get_v1_nat_entries_device_id_response_200 = cls(
            nat_entries=nat_entries,
            page_info=page_info,
            ts=ts,
        )

        get_v1_nat_entries_device_id_response_200.additional_properties = d
        return get_v1_nat_entries_device_id_response_200

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
