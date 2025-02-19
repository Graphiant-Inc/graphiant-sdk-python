from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item_data import (
        PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2ItemData,
    )


T = TypeVar("T", bound="PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item")


@_attrs_define
class PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item:
    """
    Attributes:
        data (Union[Unset, PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2ItemData]):
    """

    data: Union[Unset, "PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2ItemData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item_data import (
            PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2ItemData,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2ItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2ItemData.from_dict(_data)

        post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item = cls(
            data=data,
        )

        post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item.additional_properties = d
        return post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item

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
