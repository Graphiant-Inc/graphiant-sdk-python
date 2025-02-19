from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GlobalPrefixSetsDeviceResponse200PrefixSetsItemPoliciesItem")


@_attrs_define
class GetV1GlobalPrefixSetsDeviceResponse200PrefixSetsItemPoliciesItem:
    """
    Attributes:
        attach_point (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    attach_point: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attach_point = self.attach_point

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attach_point is not UNSET:
            field_dict["attachPoint"] = attach_point
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attach_point = d.pop("attachPoint", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_v1_global_prefix_sets_device_response_200_prefix_sets_item_policies_item = cls(
            attach_point=attach_point,
            id=id,
            name=name,
        )

        get_v1_global_prefix_sets_device_response_200_prefix_sets_item_policies_item.additional_properties = d
        return get_v1_global_prefix_sets_device_response_200_prefix_sets_item_policies_item

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
