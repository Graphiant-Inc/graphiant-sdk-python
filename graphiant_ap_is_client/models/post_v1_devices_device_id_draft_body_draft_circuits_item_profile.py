from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_profile_queues_item import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfileQueuesItem,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile:
    """
    Attributes:
        kind (Union[Unset, str]):  Example: TYPE_ENUM.
        profile (Union[Unset, str]):  Example: TYPE_ENUM.
        queues (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfileQueuesItem']]):
    """

    kind: Union[Unset, str] = UNSET
    profile: Union[Unset, str] = UNSET
    queues: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfileQueuesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        profile = self.profile

        queues: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.queues, Unset):
            queues = []
            for queues_item_data in self.queues:
                queues_item = queues_item_data.to_dict()
                queues.append(queues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if profile is not UNSET:
            field_dict["profile"] = profile
        if queues is not UNSET:
            field_dict["queues"] = queues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_profile_queues_item import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfileQueuesItem,
        )

        d = src_dict.copy()
        kind = d.pop("kind", UNSET)

        profile = d.pop("profile", UNSET)

        queues = []
        _queues = d.pop("queues", UNSET)
        for queues_item_data in _queues or []:
            queues_item = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfileQueuesItem.from_dict(queues_item_data)

            queues.append(queues_item)

        post_v1_devices_device_id_draft_body_draft_circuits_item_profile = cls(
            kind=kind,
            profile=profile,
            queues=queues,
        )

        post_v1_devices_device_id_draft_body_draft_circuits_item_profile.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_circuits_item_profile

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
