from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2ExtranetSitesConsumptionOverviewBody")


@_attrs_define
class PostV2ExtranetSitesConsumptionOverviewBody:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        is_b2b (Union[Unset, str]):  Example: TYPE_BOOL.
        is_provider (Union[Unset, str]):  Example: TYPE_BOOL.
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    id: Union[Unset, str] = UNSET
    is_b2b: Union[Unset, str] = UNSET
    is_provider: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_b2b = self.is_b2b

        is_provider = self.is_provider

        site_id = self.site_id

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_b2b is not UNSET:
            field_dict["isB2B"] = is_b2b
        if is_provider is not UNSET:
            field_dict["isProvider"] = is_provider
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_b2b = d.pop("isB2B", UNSET)

        is_provider = d.pop("isProvider", UNSET)

        site_id = d.pop("siteId", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        post_v2_extranet_sites_consumption_overview_body = cls(
            id=id,
            is_b2b=is_b2b,
            is_provider=is_provider,
            site_id=site_id,
            vrf_id=vrf_id,
        )

        post_v2_extranet_sites_consumption_overview_body.additional_properties = d
        return post_v2_extranet_sites_consumption_overview_body

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
