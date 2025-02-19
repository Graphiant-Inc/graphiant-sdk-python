from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_body_filter_item_entries_item import PostV1FlowsBodyFilterItemEntriesItem


T = TypeVar("T", bound="PostV1FlowsBodyFilterItem")


@_attrs_define
class PostV1FlowsBodyFilterItem:
    """
    Attributes:
        bin_op (Union[Unset, str]):  Example: TYPE_ENUM.
        entries (Union[Unset, list['PostV1FlowsBodyFilterItemEntriesItem']]):
    """

    bin_op: Union[Unset, str] = UNSET
    entries: Union[Unset, list["PostV1FlowsBodyFilterItemEntriesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_op = self.bin_op

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_op is not UNSET:
            field_dict["binOp"] = bin_op
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_body_filter_item_entries_item import PostV1FlowsBodyFilterItemEntriesItem

        d = src_dict.copy()
        bin_op = d.pop("binOp", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = PostV1FlowsBodyFilterItemEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        post_v1_flows_body_filter_item = cls(
            bin_op=bin_op,
            entries=entries,
        )

        post_v1_flows_body_filter_item.additional_properties = d
        return post_v1_flows_body_filter_item

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
