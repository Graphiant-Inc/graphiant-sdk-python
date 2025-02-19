from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item import (
        GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdPolicyZonepairsResponse200")


@_attrs_define
class GetV1DevicesDeviceIdPolicyZonepairsResponse200:
    """
    Attributes:
        zone_pairs (Union[Unset, list['GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem']]):
    """

    zone_pairs: Union[Unset, list["GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_pairs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.zone_pairs, Unset):
            zone_pairs = []
            for zone_pairs_item_data in self.zone_pairs:
                zone_pairs_item = zone_pairs_item_data.to_dict()
                zone_pairs.append(zone_pairs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone_pairs is not UNSET:
            field_dict["zonePairs"] = zone_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item import (
            GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem,
        )

        d = src_dict.copy()
        zone_pairs = []
        _zone_pairs = d.pop("zonePairs", UNSET)
        for zone_pairs_item_data in _zone_pairs or []:
            zone_pairs_item = GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem.from_dict(
                zone_pairs_item_data
            )

            zone_pairs.append(zone_pairs_item)

        get_v1_devices_device_id_policy_zonepairs_response_200 = cls(
            zone_pairs=zone_pairs,
        )

        get_v1_devices_device_id_policy_zonepairs_response_200.additional_properties = d
        return get_v1_devices_device_id_policy_zonepairs_response_200

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
