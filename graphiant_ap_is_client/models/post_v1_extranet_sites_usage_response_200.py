from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranet_sites_usage_response_200_dl_stats_item import (
        PostV1ExtranetSitesUsageResponse200DlStatsItem,
    )
    from ..models.post_v1_extranet_sites_usage_response_200_ul_stats_item import (
        PostV1ExtranetSitesUsageResponse200UlStatsItem,
    )


T = TypeVar("T", bound="PostV1ExtranetSitesUsageResponse200")


@_attrs_define
class PostV1ExtranetSitesUsageResponse200:
    """
    Attributes:
        dl_stats (Union[Unset, list['PostV1ExtranetSitesUsageResponse200DlStatsItem']]):
        ul_stats (Union[Unset, list['PostV1ExtranetSitesUsageResponse200UlStatsItem']]):
    """

    dl_stats: Union[Unset, list["PostV1ExtranetSitesUsageResponse200DlStatsItem"]] = UNSET
    ul_stats: Union[Unset, list["PostV1ExtranetSitesUsageResponse200UlStatsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dl_stats: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dl_stats, Unset):
            dl_stats = []
            for dl_stats_item_data in self.dl_stats:
                dl_stats_item = dl_stats_item_data.to_dict()
                dl_stats.append(dl_stats_item)

        ul_stats: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ul_stats, Unset):
            ul_stats = []
            for ul_stats_item_data in self.ul_stats:
                ul_stats_item = ul_stats_item_data.to_dict()
                ul_stats.append(ul_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dl_stats is not UNSET:
            field_dict["dlStats"] = dl_stats
        if ul_stats is not UNSET:
            field_dict["ulStats"] = ul_stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranet_sites_usage_response_200_dl_stats_item import (
            PostV1ExtranetSitesUsageResponse200DlStatsItem,
        )
        from ..models.post_v1_extranet_sites_usage_response_200_ul_stats_item import (
            PostV1ExtranetSitesUsageResponse200UlStatsItem,
        )

        d = src_dict.copy()
        dl_stats = []
        _dl_stats = d.pop("dlStats", UNSET)
        for dl_stats_item_data in _dl_stats or []:
            dl_stats_item = PostV1ExtranetSitesUsageResponse200DlStatsItem.from_dict(dl_stats_item_data)

            dl_stats.append(dl_stats_item)

        ul_stats = []
        _ul_stats = d.pop("ulStats", UNSET)
        for ul_stats_item_data in _ul_stats or []:
            ul_stats_item = PostV1ExtranetSitesUsageResponse200UlStatsItem.from_dict(ul_stats_item_data)

            ul_stats.append(ul_stats_item)

        post_v1_extranet_sites_usage_response_200 = cls(
            dl_stats=dl_stats,
            ul_stats=ul_stats,
        )

        post_v1_extranet_sites_usage_response_200.additional_properties = d
        return post_v1_extranet_sites_usage_response_200

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
