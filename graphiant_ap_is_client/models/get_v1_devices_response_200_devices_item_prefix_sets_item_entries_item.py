from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItemPrefixSetsItemEntriesItem")


@_attrs_define
class GetV1DevicesResponse200DevicesItemPrefixSetsItemEntriesItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ip_prefix (Union[Unset, str]):  Example: TYPE_STRING.
        mask_lower (Union[Unset, str]):  Example: TYPE_UINT32.
        mask_upper (Union[Unset, str]):  Example: TYPE_UINT32.
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    id: Union[Unset, str] = UNSET
    ip_prefix: Union[Unset, str] = UNSET
    mask_lower: Union[Unset, str] = UNSET
    mask_upper: Union[Unset, str] = UNSET
    seq: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ip_prefix = self.ip_prefix

        mask_lower = self.mask_lower

        mask_upper = self.mask_upper

        seq = self.seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ip_prefix is not UNSET:
            field_dict["ipPrefix"] = ip_prefix
        if mask_lower is not UNSET:
            field_dict["maskLower"] = mask_lower
        if mask_upper is not UNSET:
            field_dict["maskUpper"] = mask_upper
        if seq is not UNSET:
            field_dict["seq"] = seq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        ip_prefix = d.pop("ipPrefix", UNSET)

        mask_lower = d.pop("maskLower", UNSET)

        mask_upper = d.pop("maskUpper", UNSET)

        seq = d.pop("seq", UNSET)

        get_v1_devices_response_200_devices_item_prefix_sets_item_entries_item = cls(
            id=id,
            ip_prefix=ip_prefix,
            mask_lower=mask_lower,
            mask_upper=mask_upper,
            seq=seq,
        )

        get_v1_devices_response_200_devices_item_prefix_sets_item_entries_item.additional_properties = d
        return get_v1_devices_response_200_devices_item_prefix_sets_item_entries_item

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
