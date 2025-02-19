from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft import PostV1DevicesDeviceIdDraftBodyDraft


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBody")


@_attrs_define
class PostV1DevicesDeviceIdDraftBody:
    """
    Attributes:
        base_version (Union[Unset, str]):  Example: TYPE_INT32.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        draft (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraft]):
    """

    base_version: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    draft: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraft"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_version = self.base_version

        description = self.description

        draft: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_version is not UNSET:
            field_dict["baseVersion"] = base_version
        if description is not UNSET:
            field_dict["description"] = description
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft import PostV1DevicesDeviceIdDraftBodyDraft

        d = src_dict.copy()
        base_version = d.pop("baseVersion", UNSET)

        description = d.pop("description", UNSET)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraft]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = PostV1DevicesDeviceIdDraftBodyDraft.from_dict(_draft)

        post_v1_devices_device_id_draft_body = cls(
            base_version=base_version,
            description=description,
            draft=draft,
        )

        post_v1_devices_device_id_draft_body.additional_properties = d
        return post_v1_devices_device_id_draft_body

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
