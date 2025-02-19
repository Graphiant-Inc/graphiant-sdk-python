from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_nat_policy_nat_policy_rulesets_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicyNatPolicyRulesetsItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicy")


@_attrs_define
class GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicy:
    """
    Attributes:
        nat_policy_rulesets (Union[Unset,
            list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicyNatPolicyRulesetsItem']]):
    """

    nat_policy_rulesets: Union[
        Unset, list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicyNatPolicyRulesetsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nat_policy_rulesets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nat_policy_rulesets, Unset):
            nat_policy_rulesets = []
            for nat_policy_rulesets_item_data in self.nat_policy_rulesets:
                nat_policy_rulesets_item = nat_policy_rulesets_item_data.to_dict()
                nat_policy_rulesets.append(nat_policy_rulesets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nat_policy_rulesets is not UNSET:
            field_dict["natPolicyRulesets"] = nat_policy_rulesets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_nat_policy_nat_policy_rulesets_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicyNatPolicyRulesetsItem,
        )

        d = src_dict.copy()
        nat_policy_rulesets = []
        _nat_policy_rulesets = d.pop("natPolicyRulesets", UNSET)
        for nat_policy_rulesets_item_data in _nat_policy_rulesets or []:
            nat_policy_rulesets_item = (
                GetV1DevicesDeviceIdEdgesResponse200DevicesItemNatPolicyNatPolicyRulesetsItem.from_dict(
                    nat_policy_rulesets_item_data
                )
            )

            nat_policy_rulesets.append(nat_policy_rulesets_item)

        get_v1_devices_device_id_edges_response_200_devices_item_nat_policy = cls(
            nat_policy_rulesets=nat_policy_rulesets,
        )

        get_v1_devices_device_id_edges_response_200_devices_item_nat_policy.additional_properties = d
        return get_v1_devices_device_id_edges_response_200_devices_item_nat_policy

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
