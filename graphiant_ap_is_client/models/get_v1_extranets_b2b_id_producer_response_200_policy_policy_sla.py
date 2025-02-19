from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1ExtranetsB2BIdProducerResponse200PolicyPolicySla")


@_attrs_define
class GetV1ExtranetsB2BIdProducerResponse200PolicyPolicySla:
    """
    Attributes:
        backup_circuit (Union[Unset, str]):  Example: TYPE_ENUM.
        class_ (Union[Unset, str]):  Example: TYPE_ENUM.
        primary_circuit (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    backup_circuit: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    primary_circuit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_circuit = self.backup_circuit

        class_ = self.class_

        primary_circuit = self.primary_circuit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_circuit is not UNSET:
            field_dict["backupCircuit"] = backup_circuit
        if class_ is not UNSET:
            field_dict["class"] = class_
        if primary_circuit is not UNSET:
            field_dict["primaryCircuit"] = primary_circuit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        backup_circuit = d.pop("backupCircuit", UNSET)

        class_ = d.pop("class", UNSET)

        primary_circuit = d.pop("primaryCircuit", UNSET)

        get_v1_extranets_b2b_id_producer_response_200_policy_policy_sla = cls(
            backup_circuit=backup_circuit,
            class_=class_,
            primary_circuit=primary_circuit,
        )

        get_v1_extranets_b2b_id_producer_response_200_policy_policy_sla.additional_properties = d
        return get_v1_extranets_b2b_id_producer_response_200_policy_policy_sla

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
