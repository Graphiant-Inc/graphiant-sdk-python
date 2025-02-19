from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_ospfv_3_default_originate_response_200_default_originates_item import (
        GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200DefaultOriginatesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200")


@_attrs_define
class GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200:
    """
    Attributes:
        default_originates (Union[Unset,
            list['GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200DefaultOriginatesItem']]):
    """

    default_originates: Union[
        Unset, list["GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200DefaultOriginatesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_originates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.default_originates, Unset):
            default_originates = []
            for default_originates_item_data in self.default_originates:
                default_originates_item = default_originates_item_data.to_dict()
                default_originates.append(default_originates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_originates is not UNSET:
            field_dict["defaultOriginates"] = default_originates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_ospfv_3_default_originate_response_200_default_originates_item import (
            GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200DefaultOriginatesItem,
        )

        d = src_dict.copy()
        default_originates = []
        _default_originates = d.pop("defaultOriginates", UNSET)
        for default_originates_item_data in _default_originates or []:
            default_originates_item = (
                GetV1DevicesDeviceIdOspfv3DefaultOriginateResponse200DefaultOriginatesItem.from_dict(
                    default_originates_item_data
                )
            )

            default_originates.append(default_originates_item)

        get_v1_devices_device_id_ospfv_3_default_originate_response_200 = cls(
            default_originates=default_originates,
        )

        get_v1_devices_device_id_ospfv_3_default_originate_response_200.additional_properties = d
        return get_v1_devices_device_id_ospfv_3_default_originate_response_200

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
