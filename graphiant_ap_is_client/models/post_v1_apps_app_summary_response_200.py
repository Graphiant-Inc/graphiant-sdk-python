from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_app_summary_response_200_app_summary import PostV1AppsAppSummaryResponse200AppSummary


T = TypeVar("T", bound="PostV1AppsAppSummaryResponse200")


@_attrs_define
class PostV1AppsAppSummaryResponse200:
    """
    Attributes:
        app_summary (Union[Unset, PostV1AppsAppSummaryResponse200AppSummary]):
    """

    app_summary: Union[Unset, "PostV1AppsAppSummaryResponse200AppSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_summary, Unset):
            app_summary = self.app_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_summary is not UNSET:
            field_dict["appSummary"] = app_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_app_summary_response_200_app_summary import PostV1AppsAppSummaryResponse200AppSummary

        d = src_dict.copy()
        _app_summary = d.pop("appSummary", UNSET)
        app_summary: Union[Unset, PostV1AppsAppSummaryResponse200AppSummary]
        if isinstance(_app_summary, Unset):
            app_summary = UNSET
        else:
            app_summary = PostV1AppsAppSummaryResponse200AppSummary.from_dict(_app_summary)

        post_v1_apps_app_summary_response_200 = cls(
            app_summary=app_summary,
        )

        post_v1_apps_app_summary_response_200.additional_properties = d
        return post_v1_apps_app_summary_response_200

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
