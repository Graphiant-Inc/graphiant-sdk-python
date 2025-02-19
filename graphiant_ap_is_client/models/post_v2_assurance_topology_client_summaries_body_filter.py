from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyClientSummariesBodyFilter")


@_attrs_define
class PostV2AssuranceTopologyClientSummariesBodyFilter:
    """
    Attributes:
        client_site_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        region_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT32'].
        server_site_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
    """

    client_site_ids: Union[Unset, list[str]] = UNSET
    region_ids: Union[Unset, list[str]] = UNSET
    server_site_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_site_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.client_site_ids, Unset):
            client_site_ids = self.client_site_ids

        region_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.region_ids, Unset):
            region_ids = self.region_ids

        server_site_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.server_site_ids, Unset):
            server_site_ids = self.server_site_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_site_ids is not UNSET:
            field_dict["clientSiteIds"] = client_site_ids
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids
        if server_site_ids is not UNSET:
            field_dict["serverSiteIds"] = server_site_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        client_site_ids = cast(list[str], d.pop("clientSiteIds", UNSET))

        region_ids = cast(list[str], d.pop("regionIds", UNSET))

        server_site_ids = cast(list[str], d.pop("serverSiteIds", UNSET))

        post_v2_assurance_topology_client_summaries_body_filter = cls(
            client_site_ids=client_site_ids,
            region_ids=region_ids,
            server_site_ids=server_site_ids,
        )

        post_v2_assurance_topology_client_summaries_body_filter.additional_properties = d
        return post_v2_assurance_topology_client_summaries_body_filter

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
