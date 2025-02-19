from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1TroubleshootingEnterpriseBodyFilter")


@_attrs_define
class PostV1TroubleshootingEnterpriseBodyFilter:
    """
    Attributes:
        circuit_names (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        device_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        lan_segments (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        region_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        site_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
    """

    circuit_names: Union[Unset, list[str]] = UNSET
    device_ids: Union[Unset, list[str]] = UNSET
    lan_segments: Union[Unset, list[str]] = UNSET
    region_ids: Union[Unset, list[str]] = UNSET
    site_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.circuit_names, Unset):
            circuit_names = self.circuit_names

        device_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_ids, Unset):
            device_ids = self.device_ids

        lan_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lan_segments, Unset):
            lan_segments = self.lan_segments

        region_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.region_ids, Unset):
            region_ids = self.region_ids

        site_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.site_ids, Unset):
            site_ids = self.site_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_names is not UNSET:
            field_dict["circuitNames"] = circuit_names
        if device_ids is not UNSET:
            field_dict["deviceIds"] = device_ids
        if lan_segments is not UNSET:
            field_dict["lanSegments"] = lan_segments
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids
        if site_ids is not UNSET:
            field_dict["siteIds"] = site_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_names = cast(list[str], d.pop("circuitNames", UNSET))

        device_ids = cast(list[str], d.pop("deviceIds", UNSET))

        lan_segments = cast(list[str], d.pop("lanSegments", UNSET))

        region_ids = cast(list[str], d.pop("regionIds", UNSET))

        site_ids = cast(list[str], d.pop("siteIds", UNSET))

        post_v1_troubleshooting_enterprise_body_filter = cls(
            circuit_names=circuit_names,
            device_ids=device_ids,
            lan_segments=lan_segments,
            region_ids=region_ids,
            site_ids=site_ids,
        )

        post_v1_troubleshooting_enterprise_body_filter.additional_properties = d
        return post_v1_troubleshooting_enterprise_body_filter

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
