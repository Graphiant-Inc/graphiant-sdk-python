from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_traffic_policies_zones_item_value_zone import (
        PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValueZone,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValue:
    """
    Attributes:
        zone (Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValueZone]):
    """

    zone: Union[Unset, "PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValueZone"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.zone, Unset):
            zone = self.zone.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_traffic_policies_zones_item_value_zone import (
            PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValueZone,
        )

        d = src_dict.copy()
        _zone = d.pop("zone", UNSET)
        zone: Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValueZone]
        if isinstance(_zone, Unset):
            zone = UNSET
        else:
            zone = PatchV1GlobalConfigBodyTrafficPoliciesZonesItemValueZone.from_dict(_zone)

        patch_v1_global_config_body_traffic_policies_zones_item_value = cls(
            zone=zone,
        )

        patch_v1_global_config_body_traffic_policies_zones_item_value.additional_properties = d
        return patch_v1_global_config_body_traffic_policies_zones_item_value

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
