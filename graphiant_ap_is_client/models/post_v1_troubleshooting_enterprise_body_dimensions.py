from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1TroubleshootingEnterpriseBodyDimensions")


@_attrs_define
class PostV1TroubleshootingEnterpriseBodyDimensions:
    """
    Attributes:
        certificate_expiry (Union[Unset, str]):  Example: TYPE_BOOL.
        core_connectivity (Union[Unset, str]):  Example: TYPE_BOOL.
        core_transitions (Union[Unset, str]):  Example: TYPE_BOOL.
        cpu (Union[Unset, str]):  Example: TYPE_BOOL.
        crashes (Union[Unset, str]):  Example: TYPE_BOOL.
        credit_expiry (Union[Unset, str]):  Example: TYPE_BOOL.
        disk (Union[Unset, str]):  Example: TYPE_BOOL.
        fan_speed (Union[Unset, str]):  Example: TYPE_BOOL.
        license_expiry (Union[Unset, str]):  Example: TYPE_BOOL.
        memory (Union[Unset, str]):  Example: TYPE_BOOL.
        odp_connectivity (Union[Unset, str]):  Example: TYPE_BOOL.
        odp_transitions (Union[Unset, str]):  Example: TYPE_BOOL.
        sla_performance (Union[Unset, str]):  Example: TYPE_BOOL.
        t_2_connectivity (Union[Unset, str]):  Example: TYPE_BOOL.
        t_2_transitions (Union[Unset, str]):  Example: TYPE_BOOL.
        temperature (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    certificate_expiry: Union[Unset, str] = UNSET
    core_connectivity: Union[Unset, str] = UNSET
    core_transitions: Union[Unset, str] = UNSET
    cpu: Union[Unset, str] = UNSET
    crashes: Union[Unset, str] = UNSET
    credit_expiry: Union[Unset, str] = UNSET
    disk: Union[Unset, str] = UNSET
    fan_speed: Union[Unset, str] = UNSET
    license_expiry: Union[Unset, str] = UNSET
    memory: Union[Unset, str] = UNSET
    odp_connectivity: Union[Unset, str] = UNSET
    odp_transitions: Union[Unset, str] = UNSET
    sla_performance: Union[Unset, str] = UNSET
    t_2_connectivity: Union[Unset, str] = UNSET
    t_2_transitions: Union[Unset, str] = UNSET
    temperature: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate_expiry = self.certificate_expiry

        core_connectivity = self.core_connectivity

        core_transitions = self.core_transitions

        cpu = self.cpu

        crashes = self.crashes

        credit_expiry = self.credit_expiry

        disk = self.disk

        fan_speed = self.fan_speed

        license_expiry = self.license_expiry

        memory = self.memory

        odp_connectivity = self.odp_connectivity

        odp_transitions = self.odp_transitions

        sla_performance = self.sla_performance

        t_2_connectivity = self.t_2_connectivity

        t_2_transitions = self.t_2_transitions

        temperature = self.temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_expiry is not UNSET:
            field_dict["certificateExpiry"] = certificate_expiry
        if core_connectivity is not UNSET:
            field_dict["coreConnectivity"] = core_connectivity
        if core_transitions is not UNSET:
            field_dict["coreTransitions"] = core_transitions
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if crashes is not UNSET:
            field_dict["crashes"] = crashes
        if credit_expiry is not UNSET:
            field_dict["creditExpiry"] = credit_expiry
        if disk is not UNSET:
            field_dict["disk"] = disk
        if fan_speed is not UNSET:
            field_dict["fanSpeed"] = fan_speed
        if license_expiry is not UNSET:
            field_dict["licenseExpiry"] = license_expiry
        if memory is not UNSET:
            field_dict["memory"] = memory
        if odp_connectivity is not UNSET:
            field_dict["odpConnectivity"] = odp_connectivity
        if odp_transitions is not UNSET:
            field_dict["odpTransitions"] = odp_transitions
        if sla_performance is not UNSET:
            field_dict["slaPerformance"] = sla_performance
        if t_2_connectivity is not UNSET:
            field_dict["t2Connectivity"] = t_2_connectivity
        if t_2_transitions is not UNSET:
            field_dict["t2Transitions"] = t_2_transitions
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_expiry = d.pop("certificateExpiry", UNSET)

        core_connectivity = d.pop("coreConnectivity", UNSET)

        core_transitions = d.pop("coreTransitions", UNSET)

        cpu = d.pop("cpu", UNSET)

        crashes = d.pop("crashes", UNSET)

        credit_expiry = d.pop("creditExpiry", UNSET)

        disk = d.pop("disk", UNSET)

        fan_speed = d.pop("fanSpeed", UNSET)

        license_expiry = d.pop("licenseExpiry", UNSET)

        memory = d.pop("memory", UNSET)

        odp_connectivity = d.pop("odpConnectivity", UNSET)

        odp_transitions = d.pop("odpTransitions", UNSET)

        sla_performance = d.pop("slaPerformance", UNSET)

        t_2_connectivity = d.pop("t2Connectivity", UNSET)

        t_2_transitions = d.pop("t2Transitions", UNSET)

        temperature = d.pop("temperature", UNSET)

        post_v1_troubleshooting_enterprise_body_dimensions = cls(
            certificate_expiry=certificate_expiry,
            core_connectivity=core_connectivity,
            core_transitions=core_transitions,
            cpu=cpu,
            crashes=crashes,
            credit_expiry=credit_expiry,
            disk=disk,
            fan_speed=fan_speed,
            license_expiry=license_expiry,
            memory=memory,
            odp_connectivity=odp_connectivity,
            odp_transitions=odp_transitions,
            sla_performance=sla_performance,
            t_2_connectivity=t_2_connectivity,
            t_2_transitions=t_2_transitions,
            temperature=temperature,
        )

        post_v1_troubleshooting_enterprise_body_dimensions.additional_properties = d
        return post_v1_troubleshooting_enterprise_body_dimensions

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
