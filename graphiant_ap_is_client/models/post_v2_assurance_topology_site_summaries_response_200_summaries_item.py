from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_site_summaries_response_200_summaries_item_site import (
        PostV2AssuranceTopologySiteSummariesResponse200SummariesItemSite,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologySiteSummariesResponse200SummariesItem")


@_attrs_define
class PostV2AssuranceTopologySiteSummariesResponse200SummariesItem:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        lan_segments (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        session_count (Union[Unset, str]):  Example: TYPE_INT32.
        site (Union[Unset, PostV2AssuranceTopologySiteSummariesResponse200SummariesItemSite]):
    """

    app_name: Union[Unset, str] = UNSET
    lan_segments: Union[Unset, list[str]] = UNSET
    session_count: Union[Unset, str] = UNSET
    site: Union[Unset, "PostV2AssuranceTopologySiteSummariesResponse200SummariesItemSite"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        lan_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lan_segments, Unset):
            lan_segments = self.lan_segments

        session_count = self.session_count

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if lan_segments is not UNSET:
            field_dict["lanSegments"] = lan_segments
        if session_count is not UNSET:
            field_dict["sessionCount"] = session_count
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_site_summaries_response_200_summaries_item_site import (
            PostV2AssuranceTopologySiteSummariesResponse200SummariesItemSite,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        lan_segments = cast(list[str], d.pop("lanSegments", UNSET))

        session_count = d.pop("sessionCount", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, PostV2AssuranceTopologySiteSummariesResponse200SummariesItemSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PostV2AssuranceTopologySiteSummariesResponse200SummariesItemSite.from_dict(_site)

        post_v2_assurance_topology_site_summaries_response_200_summaries_item = cls(
            app_name=app_name,
            lan_segments=lan_segments,
            session_count=session_count,
            site=site,
        )

        post_v2_assurance_topology_site_summaries_response_200_summaries_item.additional_properties = d
        return post_v2_assurance_topology_site_summaries_response_200_summaries_item

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
