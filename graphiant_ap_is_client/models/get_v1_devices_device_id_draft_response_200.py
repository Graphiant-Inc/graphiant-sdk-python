from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_draft_response_200_draft import GetV1DevicesDeviceIdDraftResponse200Draft


T = TypeVar("T", bound="GetV1DevicesDeviceIdDraftResponse200")


@_attrs_define
class GetV1DevicesDeviceIdDraftResponse200:
    """
    Attributes:
        draft (Union[Unset, GetV1DevicesDeviceIdDraftResponse200Draft]):
    """

    draft: Union[Unset, "GetV1DevicesDeviceIdDraftResponse200Draft"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        draft: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_draft_response_200_draft import GetV1DevicesDeviceIdDraftResponse200Draft

        d = src_dict.copy()
        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, GetV1DevicesDeviceIdDraftResponse200Draft]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = GetV1DevicesDeviceIdDraftResponse200Draft.from_dict(_draft)

        get_v1_devices_device_id_draft_response_200 = cls(
            draft=draft,
        )

        get_v1_devices_device_id_draft_response_200.additional_properties = d
        return get_v1_devices_device_id_draft_response_200

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
