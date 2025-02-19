from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_site_site_id_detail_response_200_site import PostV2SiteSiteIdDetailResponse200Site
    from ..models.post_v2_site_site_id_detail_response_200_snapshots_item import (
        PostV2SiteSiteIdDetailResponse200SnapshotsItem,
    )


T = TypeVar("T", bound="PostV2SiteSiteIdDetailResponse200")


@_attrs_define
class PostV2SiteSiteIdDetailResponse200:
    """
    Attributes:
        site (Union[Unset, PostV2SiteSiteIdDetailResponse200Site]):
        snapshots (Union[Unset, list['PostV2SiteSiteIdDetailResponse200SnapshotsItem']]):
    """

    site: Union[Unset, "PostV2SiteSiteIdDetailResponse200Site"] = UNSET
    snapshots: Union[Unset, list["PostV2SiteSiteIdDetailResponse200SnapshotsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        snapshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snapshots, Unset):
            snapshots = []
            for snapshots_item_data in self.snapshots:
                snapshots_item = snapshots_item_data.to_dict()
                snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_site_site_id_detail_response_200_site import PostV2SiteSiteIdDetailResponse200Site
        from ..models.post_v2_site_site_id_detail_response_200_snapshots_item import (
            PostV2SiteSiteIdDetailResponse200SnapshotsItem,
        )

        d = src_dict.copy()
        _site = d.pop("site", UNSET)
        site: Union[Unset, PostV2SiteSiteIdDetailResponse200Site]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PostV2SiteSiteIdDetailResponse200Site.from_dict(_site)

        snapshots = []
        _snapshots = d.pop("snapshots", UNSET)
        for snapshots_item_data in _snapshots or []:
            snapshots_item = PostV2SiteSiteIdDetailResponse200SnapshotsItem.from_dict(snapshots_item_data)

            snapshots.append(snapshots_item)

        post_v2_site_site_id_detail_response_200 = cls(
            site=site,
            snapshots=snapshots,
        )

        post_v2_site_site_id_detail_response_200.additional_properties = d
        return post_v2_site_site_id_detail_response_200

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
