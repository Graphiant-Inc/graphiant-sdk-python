from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteV1PolicyRouteTagSetsIdBody")


@_attrs_define
class DeleteV1PolicyRouteTagSetsIdBody:
    """
    Attributes:
        level (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    level: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        level = d.pop("level", UNSET)

        delete_v1_policy_route_tag_sets_id_body = cls(
            level=level,
        )

        delete_v1_policy_route_tag_sets_id_body.additional_properties = d
        return delete_v1_policy_route_tag_sets_id_body

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
