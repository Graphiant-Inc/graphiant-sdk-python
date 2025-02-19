from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdEdgesResponse200DevicesItemSnmpTargetsItem")


@_attrs_define
class GetV1DevicesDeviceIdEdgesResponse200DevicesItemSnmpTargetsItem:
    """
    Attributes:
        community (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notify_filter_profile (Union[Unset, str]):  Example: TYPE_STRING.
        notify_type (Union[Unset, str]):  Example: TYPE_ENUM.
        source_ip (Union[Unset, str]):  Example: TYPE_STRING.
        target_ip (Union[Unset, str]):  Example: TYPE_STRING.
        target_type (Union[Unset, str]):  Example: TYPE_ENUM.
        usm_security_level (Union[Unset, str]):  Example: TYPE_ENUM.
        usm_user_name (Union[Unset, str]):  Example: TYPE_STRING.
        vrf_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    community: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notify_filter_profile: Union[Unset, str] = UNSET
    notify_type: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    target_ip: Union[Unset, str] = UNSET
    target_type: Union[Unset, str] = UNSET
    usm_security_level: Union[Unset, str] = UNSET
    usm_user_name: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        community = self.community

        id = self.id

        name = self.name

        notify_filter_profile = self.notify_filter_profile

        notify_type = self.notify_type

        source_ip = self.source_ip

        target_ip = self.target_ip

        target_type = self.target_type

        usm_security_level = self.usm_security_level

        usm_user_name = self.usm_user_name

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if community is not UNSET:
            field_dict["community"] = community
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if notify_filter_profile is not UNSET:
            field_dict["notifyFilterProfile"] = notify_filter_profile
        if notify_type is not UNSET:
            field_dict["notifyType"] = notify_type
        if source_ip is not UNSET:
            field_dict["sourceIp"] = source_ip
        if target_ip is not UNSET:
            field_dict["targetIp"] = target_ip
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if usm_security_level is not UNSET:
            field_dict["usmSecurityLevel"] = usm_security_level
        if usm_user_name is not UNSET:
            field_dict["usmUserName"] = usm_user_name
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        community = d.pop("community", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        notify_filter_profile = d.pop("notifyFilterProfile", UNSET)

        notify_type = d.pop("notifyType", UNSET)

        source_ip = d.pop("sourceIp", UNSET)

        target_ip = d.pop("targetIp", UNSET)

        target_type = d.pop("targetType", UNSET)

        usm_security_level = d.pop("usmSecurityLevel", UNSET)

        usm_user_name = d.pop("usmUserName", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        get_v1_devices_device_id_edges_response_200_devices_item_snmp_targets_item = cls(
            community=community,
            id=id,
            name=name,
            notify_filter_profile=notify_filter_profile,
            notify_type=notify_type,
            source_ip=source_ip,
            target_ip=target_ip,
            target_type=target_type,
            usm_security_level=usm_security_level,
            usm_user_name=usm_user_name,
            vrf_name=vrf_name,
        )

        get_v1_devices_device_id_edges_response_200_devices_item_snmp_targets_item.additional_properties = d
        return get_v1_devices_device_id_edges_response_200_devices_item_snmp_targets_item

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
