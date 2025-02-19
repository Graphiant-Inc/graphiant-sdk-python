from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_consumers_usage_top_response_200_top_consumers_item import (
        PostV2ExtranetConsumersUsageTopResponse200TopConsumersItem,
    )


T = TypeVar("T", bound="PostV2ExtranetConsumersUsageTopResponse200")


@_attrs_define
class PostV2ExtranetConsumersUsageTopResponse200:
    """
    Attributes:
        top_consumers (Union[Unset, list['PostV2ExtranetConsumersUsageTopResponse200TopConsumersItem']]):
    """

    top_consumers: Union[Unset, list["PostV2ExtranetConsumersUsageTopResponse200TopConsumersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_consumers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_consumers, Unset):
            top_consumers = []
            for top_consumers_item_data in self.top_consumers:
                top_consumers_item = top_consumers_item_data.to_dict()
                top_consumers.append(top_consumers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_consumers is not UNSET:
            field_dict["topConsumers"] = top_consumers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_consumers_usage_top_response_200_top_consumers_item import (
            PostV2ExtranetConsumersUsageTopResponse200TopConsumersItem,
        )

        d = src_dict.copy()
        top_consumers = []
        _top_consumers = d.pop("topConsumers", UNSET)
        for top_consumers_item_data in _top_consumers or []:
            top_consumers_item = PostV2ExtranetConsumersUsageTopResponse200TopConsumersItem.from_dict(
                top_consumers_item_data
            )

            top_consumers.append(top_consumers_item)

        post_v2_extranet_consumers_usage_top_response_200 = cls(
            top_consumers=top_consumers,
        )

        post_v2_extranet_consumers_usage_top_response_200.additional_properties = d
        return post_v2_extranet_consumers_usage_top_response_200

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
