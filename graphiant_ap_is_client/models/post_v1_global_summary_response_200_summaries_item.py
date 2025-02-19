from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalSummaryResponse200SummariesItem")


@_attrs_define
class PostV1GlobalSummaryResponse200SummariesItem:
    """
    Attributes:
        attach_point (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ip_version (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        num_attached_devices (Union[Unset, str]):  Example: TYPE_UINT32.
        num_attached_sites (Union[Unset, str]):  Example: TYPE_UINT32.
        num_failures (Union[Unset, str]):  Example: TYPE_UINT32.
        num_in_sync_devices (Union[Unset, str]):  Example: TYPE_UINT32.
        num_override_devices (Union[Unset, str]):  Example: TYPE_UINT32.
        num_policies (Union[Unset, str]):  Example: TYPE_UINT32.
        num_prefixes (Union[Unset, str]):  Example: TYPE_UINT32.
        num_rules (Union[Unset, str]):  Example: TYPE_UINT32.
        num_statements (Union[Unset, str]):  Example: TYPE_UINT32.
        traffic_policy_type (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    attach_point: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_version: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    num_attached_devices: Union[Unset, str] = UNSET
    num_attached_sites: Union[Unset, str] = UNSET
    num_failures: Union[Unset, str] = UNSET
    num_in_sync_devices: Union[Unset, str] = UNSET
    num_override_devices: Union[Unset, str] = UNSET
    num_policies: Union[Unset, str] = UNSET
    num_prefixes: Union[Unset, str] = UNSET
    num_rules: Union[Unset, str] = UNSET
    num_statements: Union[Unset, str] = UNSET
    traffic_policy_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attach_point = self.attach_point

        id = self.id

        ip_version = self.ip_version

        name = self.name

        num_attached_devices = self.num_attached_devices

        num_attached_sites = self.num_attached_sites

        num_failures = self.num_failures

        num_in_sync_devices = self.num_in_sync_devices

        num_override_devices = self.num_override_devices

        num_policies = self.num_policies

        num_prefixes = self.num_prefixes

        num_rules = self.num_rules

        num_statements = self.num_statements

        traffic_policy_type = self.traffic_policy_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attach_point is not UNSET:
            field_dict["attachPoint"] = attach_point
        if id is not UNSET:
            field_dict["id"] = id
        if ip_version is not UNSET:
            field_dict["ipVersion"] = ip_version
        if name is not UNSET:
            field_dict["name"] = name
        if num_attached_devices is not UNSET:
            field_dict["numAttachedDevices"] = num_attached_devices
        if num_attached_sites is not UNSET:
            field_dict["numAttachedSites"] = num_attached_sites
        if num_failures is not UNSET:
            field_dict["numFailures"] = num_failures
        if num_in_sync_devices is not UNSET:
            field_dict["numInSyncDevices"] = num_in_sync_devices
        if num_override_devices is not UNSET:
            field_dict["numOverrideDevices"] = num_override_devices
        if num_policies is not UNSET:
            field_dict["numPolicies"] = num_policies
        if num_prefixes is not UNSET:
            field_dict["numPrefixes"] = num_prefixes
        if num_rules is not UNSET:
            field_dict["numRules"] = num_rules
        if num_statements is not UNSET:
            field_dict["numStatements"] = num_statements
        if traffic_policy_type is not UNSET:
            field_dict["trafficPolicyType"] = traffic_policy_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attach_point = d.pop("attachPoint", UNSET)

        id = d.pop("id", UNSET)

        ip_version = d.pop("ipVersion", UNSET)

        name = d.pop("name", UNSET)

        num_attached_devices = d.pop("numAttachedDevices", UNSET)

        num_attached_sites = d.pop("numAttachedSites", UNSET)

        num_failures = d.pop("numFailures", UNSET)

        num_in_sync_devices = d.pop("numInSyncDevices", UNSET)

        num_override_devices = d.pop("numOverrideDevices", UNSET)

        num_policies = d.pop("numPolicies", UNSET)

        num_prefixes = d.pop("numPrefixes", UNSET)

        num_rules = d.pop("numRules", UNSET)

        num_statements = d.pop("numStatements", UNSET)

        traffic_policy_type = d.pop("trafficPolicyType", UNSET)

        post_v1_global_summary_response_200_summaries_item = cls(
            attach_point=attach_point,
            id=id,
            ip_version=ip_version,
            name=name,
            num_attached_devices=num_attached_devices,
            num_attached_sites=num_attached_sites,
            num_failures=num_failures,
            num_in_sync_devices=num_in_sync_devices,
            num_override_devices=num_override_devices,
            num_policies=num_policies,
            num_prefixes=num_prefixes,
            num_rules=num_rules,
            num_statements=num_statements,
            traffic_policy_type=traffic_policy_type,
        )

        post_v1_global_summary_response_200_summaries_item.additional_properties = d
        return post_v1_global_summary_response_200_summaries_item

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
