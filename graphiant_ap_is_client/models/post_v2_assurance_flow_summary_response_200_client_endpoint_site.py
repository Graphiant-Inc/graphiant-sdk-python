from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceFlowSummaryResponse200ClientEndpointSite")


@_attrs_define
class PostV2AssuranceFlowSummaryResponse200ClientEndpointSite:
    """
    Attributes:
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    site_id: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        site_name = self.site_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        post_v2_assurance_flow_summary_response_200_client_endpoint_site = cls(
            site_id=site_id,
            site_name=site_name,
        )

        post_v2_assurance_flow_summary_response_200_client_endpoint_site.additional_properties = d
        return post_v2_assurance_flow_summary_response_200_client_endpoint_site

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
