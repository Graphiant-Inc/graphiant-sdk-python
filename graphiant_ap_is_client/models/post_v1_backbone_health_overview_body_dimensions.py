from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BackboneHealthOverviewBodyDimensions")


@_attrs_define
class PostV1BackboneHealthOverviewBodyDimensions:
    """
    Attributes:
        certificate_expiry (Union[Unset, str]):  Example: TYPE_BOOL.
        core_connectivity (Union[Unset, str]):  Example: TYPE_BOOL.
        core_core_sla_performance (Union[Unset, str]):  Example: TYPE_BOOL.
        core_wan_performance (Union[Unset, str]):  Example: TYPE_BOOL.
        cpu (Union[Unset, str]):  Example: TYPE_BOOL.
        crashes (Union[Unset, str]):  Example: TYPE_BOOL.
        credit_expiry (Union[Unset, str]):  Example: TYPE_BOOL.
        disk (Union[Unset, str]):  Example: TYPE_BOOL.
        fan_speed (Union[Unset, str]):  Example: TYPE_BOOL.
        license_expiry (Union[Unset, str]):  Example: TYPE_BOOL.
        memory (Union[Unset, str]):  Example: TYPE_BOOL.
        odp_connectivity (Union[Unset, str]):  Example: TYPE_BOOL.
        t_2_connectivity (Union[Unset, str]):  Example: TYPE_BOOL.
        temperature (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    certificate_expiry: Union[Unset, str] = UNSET
    core_connectivity: Union[Unset, str] = UNSET
    core_core_sla_performance: Union[Unset, str] = UNSET
    core_wan_performance: Union[Unset, str] = UNSET
    cpu: Union[Unset, str] = UNSET
    crashes: Union[Unset, str] = UNSET
    credit_expiry: Union[Unset, str] = UNSET
    disk: Union[Unset, str] = UNSET
    fan_speed: Union[Unset, str] = UNSET
    license_expiry: Union[Unset, str] = UNSET
    memory: Union[Unset, str] = UNSET
    odp_connectivity: Union[Unset, str] = UNSET
    t_2_connectivity: Union[Unset, str] = UNSET
    temperature: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate_expiry = self.certificate_expiry

        core_connectivity = self.core_connectivity

        core_core_sla_performance = self.core_core_sla_performance

        core_wan_performance = self.core_wan_performance

        cpu = self.cpu

        crashes = self.crashes

        credit_expiry = self.credit_expiry

        disk = self.disk

        fan_speed = self.fan_speed

        license_expiry = self.license_expiry

        memory = self.memory

        odp_connectivity = self.odp_connectivity

        t_2_connectivity = self.t_2_connectivity

        temperature = self.temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_expiry is not UNSET:
            field_dict["certificateExpiry"] = certificate_expiry
        if core_connectivity is not UNSET:
            field_dict["coreConnectivity"] = core_connectivity
        if core_core_sla_performance is not UNSET:
            field_dict["coreCoreSlaPerformance"] = core_core_sla_performance
        if core_wan_performance is not UNSET:
            field_dict["coreWanPerformance"] = core_wan_performance
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
        if t_2_connectivity is not UNSET:
            field_dict["t2Connectivity"] = t_2_connectivity
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_expiry = d.pop("certificateExpiry", UNSET)

        core_connectivity = d.pop("coreConnectivity", UNSET)

        core_core_sla_performance = d.pop("coreCoreSlaPerformance", UNSET)

        core_wan_performance = d.pop("coreWanPerformance", UNSET)

        cpu = d.pop("cpu", UNSET)

        crashes = d.pop("crashes", UNSET)

        credit_expiry = d.pop("creditExpiry", UNSET)

        disk = d.pop("disk", UNSET)

        fan_speed = d.pop("fanSpeed", UNSET)

        license_expiry = d.pop("licenseExpiry", UNSET)

        memory = d.pop("memory", UNSET)

        odp_connectivity = d.pop("odpConnectivity", UNSET)

        t_2_connectivity = d.pop("t2Connectivity", UNSET)

        temperature = d.pop("temperature", UNSET)

        post_v1_backbone_health_overview_body_dimensions = cls(
            certificate_expiry=certificate_expiry,
            core_connectivity=core_connectivity,
            core_core_sla_performance=core_core_sla_performance,
            core_wan_performance=core_wan_performance,
            cpu=cpu,
            crashes=crashes,
            credit_expiry=credit_expiry,
            disk=disk,
            fan_speed=fan_speed,
            license_expiry=license_expiry,
            memory=memory,
            odp_connectivity=odp_connectivity,
            t_2_connectivity=t_2_connectivity,
            temperature=temperature,
        )

        post_v1_backbone_health_overview_body_dimensions.additional_properties = d
        return post_v1_backbone_health_overview_body_dimensions

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
