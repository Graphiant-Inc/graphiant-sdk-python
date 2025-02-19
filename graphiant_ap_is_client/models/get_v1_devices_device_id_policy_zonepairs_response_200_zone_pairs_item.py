from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item_security_rulesets_item import (
        GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItemSecurityRulesetsItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem")


@_attrs_define
class GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItem:
    """
    Attributes:
        inside (Union[Unset, str]):  Example: TYPE_STRING.
        outside (Union[Unset, str]):  Example: TYPE_STRING.
        security_rulesets (Union[Unset,
            list['GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItemSecurityRulesetsItem']]):
    """

    inside: Union[Unset, str] = UNSET
    outside: Union[Unset, str] = UNSET
    security_rulesets: Union[
        Unset, list["GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItemSecurityRulesetsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inside = self.inside

        outside = self.outside

        security_rulesets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.security_rulesets, Unset):
            security_rulesets = []
            for security_rulesets_item_data in self.security_rulesets:
                security_rulesets_item = security_rulesets_item_data.to_dict()
                security_rulesets.append(security_rulesets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inside is not UNSET:
            field_dict["inside"] = inside
        if outside is not UNSET:
            field_dict["outside"] = outside
        if security_rulesets is not UNSET:
            field_dict["securityRulesets"] = security_rulesets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item_security_rulesets_item import (
            GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItemSecurityRulesetsItem,
        )

        d = src_dict.copy()
        inside = d.pop("inside", UNSET)

        outside = d.pop("outside", UNSET)

        security_rulesets = []
        _security_rulesets = d.pop("securityRulesets", UNSET)
        for security_rulesets_item_data in _security_rulesets or []:
            security_rulesets_item = (
                GetV1DevicesDeviceIdPolicyZonepairsResponse200ZonePairsItemSecurityRulesetsItem.from_dict(
                    security_rulesets_item_data
                )
            )

            security_rulesets.append(security_rulesets_item)

        get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item = cls(
            inside=inside,
            outside=outside,
            security_rulesets=security_rulesets,
        )

        get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item.additional_properties = d
        return get_v1_devices_device_id_policy_zonepairs_response_200_zone_pairs_item

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
