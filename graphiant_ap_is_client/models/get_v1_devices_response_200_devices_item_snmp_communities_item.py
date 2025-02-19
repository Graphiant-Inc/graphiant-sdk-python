from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItemSnmpCommunitiesItem")


@_attrs_define
class GetV1DevicesResponse200DevicesItemSnmpCommunitiesItem:
    """
    Attributes:
        community_string (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    community_string: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        community_string = self.community_string

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if community_string is not UNSET:
            field_dict["communityString"] = community_string
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        community_string = d.pop("communityString", UNSET)

        id = d.pop("id", UNSET)

        get_v1_devices_response_200_devices_item_snmp_communities_item = cls(
            community_string=community_string,
            id=id,
        )

        get_v1_devices_response_200_devices_item_snmp_communities_item.additional_properties = d
        return get_v1_devices_response_200_devices_item_snmp_communities_item

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
