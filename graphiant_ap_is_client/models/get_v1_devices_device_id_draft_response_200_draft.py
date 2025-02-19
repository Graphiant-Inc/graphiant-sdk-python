from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_draft_response_200_draft_mana_device import (
        GetV1DevicesDeviceIdDraftResponse200DraftManaDevice,
    )
    from ..models.get_v1_devices_device_id_draft_response_200_draft_version_info import (
        GetV1DevicesDeviceIdDraftResponse200DraftVersionInfo,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdDraftResponse200Draft")


@_attrs_define
class GetV1DevicesDeviceIdDraftResponse200Draft:
    """
    Attributes:
        mana_device (Union[Unset, GetV1DevicesDeviceIdDraftResponse200DraftManaDevice]):
        version_info (Union[Unset, GetV1DevicesDeviceIdDraftResponse200DraftVersionInfo]):
    """

    mana_device: Union[Unset, "GetV1DevicesDeviceIdDraftResponse200DraftManaDevice"] = UNSET
    version_info: Union[Unset, "GetV1DevicesDeviceIdDraftResponse200DraftVersionInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mana_device: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mana_device, Unset):
            mana_device = self.mana_device.to_dict()

        version_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.version_info, Unset):
            version_info = self.version_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mana_device is not UNSET:
            field_dict["manaDevice"] = mana_device
        if version_info is not UNSET:
            field_dict["versionInfo"] = version_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_draft_response_200_draft_mana_device import (
            GetV1DevicesDeviceIdDraftResponse200DraftManaDevice,
        )
        from ..models.get_v1_devices_device_id_draft_response_200_draft_version_info import (
            GetV1DevicesDeviceIdDraftResponse200DraftVersionInfo,
        )

        d = src_dict.copy()
        _mana_device = d.pop("manaDevice", UNSET)
        mana_device: Union[Unset, GetV1DevicesDeviceIdDraftResponse200DraftManaDevice]
        if isinstance(_mana_device, Unset):
            mana_device = UNSET
        else:
            mana_device = GetV1DevicesDeviceIdDraftResponse200DraftManaDevice.from_dict(_mana_device)

        _version_info = d.pop("versionInfo", UNSET)
        version_info: Union[Unset, GetV1DevicesDeviceIdDraftResponse200DraftVersionInfo]
        if isinstance(_version_info, Unset):
            version_info = UNSET
        else:
            version_info = GetV1DevicesDeviceIdDraftResponse200DraftVersionInfo.from_dict(_version_info)

        get_v1_devices_device_id_draft_response_200_draft = cls(
            mana_device=mana_device,
            version_info=version_info,
        )

        get_v1_devices_device_id_draft_response_200_draft.additional_properties = d
        return get_v1_devices_device_id_draft_response_200_draft

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
