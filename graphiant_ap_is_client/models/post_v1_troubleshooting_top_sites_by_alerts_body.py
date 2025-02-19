from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_top_sites_by_alerts_body_filter import (
        PostV1TroubleshootingTopSitesByAlertsBodyFilter,
    )


T = TypeVar("T", bound="PostV1TroubleshootingTopSitesByAlertsBody")


@_attrs_define
class PostV1TroubleshootingTopSitesByAlertsBody:
    """
    Attributes:
        filter_ (Union[Unset, PostV1TroubleshootingTopSitesByAlertsBodyFilter]):
    """

    filter_: Union[Unset, "PostV1TroubleshootingTopSitesByAlertsBodyFilter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_top_sites_by_alerts_body_filter import (
            PostV1TroubleshootingTopSitesByAlertsBodyFilter,
        )

        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, PostV1TroubleshootingTopSitesByAlertsBodyFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostV1TroubleshootingTopSitesByAlertsBodyFilter.from_dict(_filter_)

        post_v1_troubleshooting_top_sites_by_alerts_body = cls(
            filter_=filter_,
        )

        post_v1_troubleshooting_top_sites_by_alerts_body.additional_properties = d
        return post_v1_troubleshooting_top_sites_by_alerts_body

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
