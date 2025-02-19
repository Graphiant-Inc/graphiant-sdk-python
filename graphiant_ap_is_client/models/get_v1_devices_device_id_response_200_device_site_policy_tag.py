from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_response_200_device_site_policy_tag_level_one import (
        GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelOne,
    )
    from ..models.get_v1_devices_device_id_response_200_device_site_policy_tag_level_two import (
        GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelTwo,
    )
    from ..models.get_v1_devices_device_id_response_200_device_site_policy_tag_level_zero import (
        GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelZero,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdResponse200DeviceSitePolicyTag")


@_attrs_define
class GetV1DevicesDeviceIdResponse200DeviceSitePolicyTag:
    """
    Attributes:
        level_one (Union[Unset, GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelOne]):
        level_two (Union[Unset, GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelTwo]):
        level_zero (Union[Unset, GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelZero]):
    """

    level_one: Union[Unset, "GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelOne"] = UNSET
    level_two: Union[Unset, "GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelTwo"] = UNSET
    level_zero: Union[Unset, "GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelZero"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level_one: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level_one, Unset):
            level_one = self.level_one.to_dict()

        level_two: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level_two, Unset):
            level_two = self.level_two.to_dict()

        level_zero: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level_zero, Unset):
            level_zero = self.level_zero.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level_one is not UNSET:
            field_dict["levelOne"] = level_one
        if level_two is not UNSET:
            field_dict["levelTwo"] = level_two
        if level_zero is not UNSET:
            field_dict["levelZero"] = level_zero

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_response_200_device_site_policy_tag_level_one import (
            GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelOne,
        )
        from ..models.get_v1_devices_device_id_response_200_device_site_policy_tag_level_two import (
            GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelTwo,
        )
        from ..models.get_v1_devices_device_id_response_200_device_site_policy_tag_level_zero import (
            GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelZero,
        )

        d = src_dict.copy()
        _level_one = d.pop("levelOne", UNSET)
        level_one: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelOne]
        if isinstance(_level_one, Unset):
            level_one = UNSET
        else:
            level_one = GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelOne.from_dict(_level_one)

        _level_two = d.pop("levelTwo", UNSET)
        level_two: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelTwo]
        if isinstance(_level_two, Unset):
            level_two = UNSET
        else:
            level_two = GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelTwo.from_dict(_level_two)

        _level_zero = d.pop("levelZero", UNSET)
        level_zero: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelZero]
        if isinstance(_level_zero, Unset):
            level_zero = UNSET
        else:
            level_zero = GetV1DevicesDeviceIdResponse200DeviceSitePolicyTagLevelZero.from_dict(_level_zero)

        get_v1_devices_device_id_response_200_device_site_policy_tag = cls(
            level_one=level_one,
            level_two=level_two,
            level_zero=level_zero,
        )

        get_v1_devices_device_id_response_200_device_site_policy_tag.additional_properties = d
        return get_v1_devices_device_id_response_200_device_site_policy_tag

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
