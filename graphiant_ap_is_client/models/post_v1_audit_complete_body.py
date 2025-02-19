from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_audit_complete_body_entry import PostV1AuditCompleteBodyEntry


T = TypeVar("T", bound="PostV1AuditCompleteBody")


@_attrs_define
class PostV1AuditCompleteBody:
    """
    Attributes:
        entry (Union[Unset, PostV1AuditCompleteBodyEntry]):
        id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    entry: Union[Unset, "PostV1AuditCompleteBodyEntry"] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_audit_complete_body_entry import PostV1AuditCompleteBodyEntry

        d = src_dict.copy()
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, PostV1AuditCompleteBodyEntry]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = PostV1AuditCompleteBodyEntry.from_dict(_entry)

        id = d.pop("id", UNSET)

        post_v1_audit_complete_body = cls(
            entry=entry,
            id=id,
        )

        post_v1_audit_complete_body.additional_properties = d
        return post_v1_audit_complete_body

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
