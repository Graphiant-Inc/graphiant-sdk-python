from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_body_time_window import (
        PostV2AssuranceUnclassifiedapplicationprofilesummaryBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2AssuranceUnclassifiedapplicationprofilesummaryBody")


@_attrs_define
class PostV2AssuranceUnclassifiedapplicationprofilesummaryBody:
    """
    Attributes:
        time_window (Union[Unset, PostV2AssuranceUnclassifiedapplicationprofilesummaryBodyTimeWindow]):
    """

    time_window: Union[Unset, "PostV2AssuranceUnclassifiedapplicationprofilesummaryBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_unclassifiedapplicationprofilesummary_body_time_window import (
            PostV2AssuranceUnclassifiedapplicationprofilesummaryBodyTimeWindow,
        )

        d = src_dict.copy()
        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceUnclassifiedapplicationprofilesummaryBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceUnclassifiedapplicationprofilesummaryBodyTimeWindow.from_dict(_time_window)

        post_v2_assurance_unclassifiedapplicationprofilesummary_body = cls(
            time_window=time_window,
        )

        post_v2_assurance_unclassifiedapplicationprofilesummary_body.additional_properties = d
        return post_v2_assurance_unclassifiedapplicationprofilesummary_body

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
