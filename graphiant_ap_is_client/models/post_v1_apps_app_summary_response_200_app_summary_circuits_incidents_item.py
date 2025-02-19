from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item_data_item import (
        PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItemDataItem,
    )


T = TypeVar("T", bound="PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem")


@_attrs_define
class PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem:
    """
    Attributes:
        data (Union[Unset, list['PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItemDataItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    data: Union[Unset, list["PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItemDataItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item_data_item import (
            PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItemDataItem,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItemDataItem.from_dict(data_item_data)

            data.append(data_item)

        name = d.pop("name", UNSET)

        post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item = cls(
            data=data,
            name=name,
        )

        post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item.additional_properties = d
        return post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item

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
