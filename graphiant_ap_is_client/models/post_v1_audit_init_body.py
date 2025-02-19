from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_audit_init_body_entry import PostV1AuditInitBodyEntry


T = TypeVar("T", bound="PostV1AuditInitBody")


@_attrs_define
class PostV1AuditInitBody:
    """
    Attributes:
        entry (Union[Unset, PostV1AuditInitBodyEntry]):
    """

    entry: Union[Unset, "PostV1AuditInitBodyEntry"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_audit_init_body_entry import PostV1AuditInitBodyEntry

        d = src_dict.copy()
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, PostV1AuditInitBodyEntry]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = PostV1AuditInitBodyEntry.from_dict(_entry)

        post_v1_audit_init_body = cls(
            entry=entry,
        )

        post_v1_audit_init_body.additional_properties = d
        return post_v1_audit_init_body

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
