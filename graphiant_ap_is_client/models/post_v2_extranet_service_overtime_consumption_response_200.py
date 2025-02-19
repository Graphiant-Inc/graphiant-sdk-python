from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_service_overtime_consumption_response_200_dl_agg_stats_item import (
        PostV2ExtranetServiceOvertimeConsumptionResponse200DlAggStatsItem,
    )
    from ..models.post_v2_extranet_service_overtime_consumption_response_200_ul_agg_stats_item import (
        PostV2ExtranetServiceOvertimeConsumptionResponse200UlAggStatsItem,
    )


T = TypeVar("T", bound="PostV2ExtranetServiceOvertimeConsumptionResponse200")


@_attrs_define
class PostV2ExtranetServiceOvertimeConsumptionResponse200:
    """
    Attributes:
        dl_agg_stats (Union[Unset, list['PostV2ExtranetServiceOvertimeConsumptionResponse200DlAggStatsItem']]):
        ul_agg_stats (Union[Unset, list['PostV2ExtranetServiceOvertimeConsumptionResponse200UlAggStatsItem']]):
    """

    dl_agg_stats: Union[Unset, list["PostV2ExtranetServiceOvertimeConsumptionResponse200DlAggStatsItem"]] = UNSET
    ul_agg_stats: Union[Unset, list["PostV2ExtranetServiceOvertimeConsumptionResponse200UlAggStatsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dl_agg_stats: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dl_agg_stats, Unset):
            dl_agg_stats = []
            for dl_agg_stats_item_data in self.dl_agg_stats:
                dl_agg_stats_item = dl_agg_stats_item_data.to_dict()
                dl_agg_stats.append(dl_agg_stats_item)

        ul_agg_stats: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ul_agg_stats, Unset):
            ul_agg_stats = []
            for ul_agg_stats_item_data in self.ul_agg_stats:
                ul_agg_stats_item = ul_agg_stats_item_data.to_dict()
                ul_agg_stats.append(ul_agg_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dl_agg_stats is not UNSET:
            field_dict["dlAggStats"] = dl_agg_stats
        if ul_agg_stats is not UNSET:
            field_dict["ulAggStats"] = ul_agg_stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_service_overtime_consumption_response_200_dl_agg_stats_item import (
            PostV2ExtranetServiceOvertimeConsumptionResponse200DlAggStatsItem,
        )
        from ..models.post_v2_extranet_service_overtime_consumption_response_200_ul_agg_stats_item import (
            PostV2ExtranetServiceOvertimeConsumptionResponse200UlAggStatsItem,
        )

        d = src_dict.copy()
        dl_agg_stats = []
        _dl_agg_stats = d.pop("dlAggStats", UNSET)
        for dl_agg_stats_item_data in _dl_agg_stats or []:
            dl_agg_stats_item = PostV2ExtranetServiceOvertimeConsumptionResponse200DlAggStatsItem.from_dict(
                dl_agg_stats_item_data
            )

            dl_agg_stats.append(dl_agg_stats_item)

        ul_agg_stats = []
        _ul_agg_stats = d.pop("ulAggStats", UNSET)
        for ul_agg_stats_item_data in _ul_agg_stats or []:
            ul_agg_stats_item = PostV2ExtranetServiceOvertimeConsumptionResponse200UlAggStatsItem.from_dict(
                ul_agg_stats_item_data
            )

            ul_agg_stats.append(ul_agg_stats_item)

        post_v2_extranet_service_overtime_consumption_response_200 = cls(
            dl_agg_stats=dl_agg_stats,
            ul_agg_stats=ul_agg_stats,
        )

        post_v2_extranet_service_overtime_consumption_response_200.additional_properties = d
        return post_v2_extranet_service_overtime_consumption_response_200

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
