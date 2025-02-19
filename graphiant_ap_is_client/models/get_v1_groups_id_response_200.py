from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_groups_id_response_200_group import GetV1GroupsIdResponse200Group


T = TypeVar("T", bound="GetV1GroupsIdResponse200")


@_attrs_define
class GetV1GroupsIdResponse200:
    """
    Attributes:
        group (Union[Unset, GetV1GroupsIdResponse200Group]):
    """

    group: Union[Unset, "GetV1GroupsIdResponse200Group"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_groups_id_response_200_group import GetV1GroupsIdResponse200Group

        d = src_dict.copy()
        _group = d.pop("group", UNSET)
        group: Union[Unset, GetV1GroupsIdResponse200Group]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = GetV1GroupsIdResponse200Group.from_dict(_group)

        get_v1_groups_id_response_200 = cls(
            group=group,
        )

        get_v1_groups_id_response_200.additional_properties = d
        return get_v1_groups_id_response_200

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
