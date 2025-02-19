from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_traffic_policies_zone_firewalls_item_value_zone_firewall import (
        PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValueZoneFirewall,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValue:
    """
    Attributes:
        zone_firewall (Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValueZoneFirewall]):
    """

    zone_firewall: Union[Unset, "PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValueZoneFirewall"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_firewall: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.zone_firewall, Unset):
            zone_firewall = self.zone_firewall.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone_firewall is not UNSET:
            field_dict["zoneFirewall"] = zone_firewall

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_traffic_policies_zone_firewalls_item_value_zone_firewall import (
            PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValueZoneFirewall,
        )

        d = src_dict.copy()
        _zone_firewall = d.pop("zoneFirewall", UNSET)
        zone_firewall: Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValueZoneFirewall]
        if isinstance(_zone_firewall, Unset):
            zone_firewall = UNSET
        else:
            zone_firewall = PatchV1GlobalConfigBodyTrafficPoliciesZoneFirewallsItemValueZoneFirewall.from_dict(
                _zone_firewall
            )

        patch_v1_global_config_body_traffic_policies_zone_firewalls_item_value = cls(
            zone_firewall=zone_firewall,
        )

        patch_v1_global_config_body_traffic_policies_zone_firewalls_item_value.additional_properties = d
        return patch_v1_global_config_body_traffic_policies_zone_firewalls_item_value

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
