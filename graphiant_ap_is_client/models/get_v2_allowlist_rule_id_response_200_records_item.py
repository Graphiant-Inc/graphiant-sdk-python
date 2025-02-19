from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV2AllowlistRuleIdResponse200RecordsItem")


@_attrs_define
class GetV2AllowlistRuleIdResponse200RecordsItem:
    """
    Attributes:
        create_time (Union[Unset, str]):  Example: TYPE_INT64.
        device_interface (Union[Unset, str]):  Example: TYPE_STRING.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_name (Union[Unset, str]):  Example: TYPE_STRING.
        entity_id (Union[Unset, str]):  Example: TYPE_STRING.
        is_wan_circuit (Union[Unset, str]):  Example: TYPE_BOOL.
        note_text (Union[Unset, str]):  Example: TYPE_STRING.
        peer_device_interface (Union[Unset, str]):  Example: TYPE_STRING.
        peer_device_name (Union[Unset, str]):  Example: TYPE_STRING.
        rule_id (Union[Unset, str]):  Example: TYPE_STRING.
        rule_name (Union[Unset, str]):  Example: TYPE_STRING.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        vrf_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    create_time: Union[Unset, str] = UNSET
    device_interface: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    enterprise_name: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    is_wan_circuit: Union[Unset, str] = UNSET
    note_text: Union[Unset, str] = UNSET
    peer_device_interface: Union[Unset, str] = UNSET
    peer_device_name: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    rule_name: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time

        device_interface = self.device_interface

        device_name = self.device_name

        enterprise_name = self.enterprise_name

        entity_id = self.entity_id

        is_wan_circuit = self.is_wan_circuit

        note_text = self.note_text

        peer_device_interface = self.peer_device_interface

        peer_device_name = self.peer_device_name

        rule_id = self.rule_id

        rule_name = self.rule_name

        site_name = self.site_name

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if device_interface is not UNSET:
            field_dict["deviceInterface"] = device_interface
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if enterprise_name is not UNSET:
            field_dict["enterpriseName"] = enterprise_name
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if is_wan_circuit is not UNSET:
            field_dict["isWanCircuit"] = is_wan_circuit
        if note_text is not UNSET:
            field_dict["noteText"] = note_text
        if peer_device_interface is not UNSET:
            field_dict["peerDeviceInterface"] = peer_device_interface
        if peer_device_name is not UNSET:
            field_dict["peerDeviceName"] = peer_device_name
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        create_time = d.pop("createTime", UNSET)

        device_interface = d.pop("deviceInterface", UNSET)

        device_name = d.pop("deviceName", UNSET)

        enterprise_name = d.pop("enterpriseName", UNSET)

        entity_id = d.pop("entityId", UNSET)

        is_wan_circuit = d.pop("isWanCircuit", UNSET)

        note_text = d.pop("noteText", UNSET)

        peer_device_interface = d.pop("peerDeviceInterface", UNSET)

        peer_device_name = d.pop("peerDeviceName", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        rule_name = d.pop("ruleName", UNSET)

        site_name = d.pop("siteName", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        get_v2_allowlist_rule_id_response_200_records_item = cls(
            create_time=create_time,
            device_interface=device_interface,
            device_name=device_name,
            enterprise_name=enterprise_name,
            entity_id=entity_id,
            is_wan_circuit=is_wan_circuit,
            note_text=note_text,
            peer_device_interface=peer_device_interface,
            peer_device_name=peer_device_name,
            rule_id=rule_id,
            rule_name=rule_name,
            site_name=site_name,
            vrf_id=vrf_id,
        )

        get_v2_allowlist_rule_id_response_200_records_item.additional_properties = d
        return get_v2_allowlist_rule_id_response_200_records_item

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
