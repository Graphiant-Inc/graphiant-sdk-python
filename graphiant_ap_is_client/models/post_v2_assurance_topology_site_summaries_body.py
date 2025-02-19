from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_site_summaries_body_filter import (
        PostV2AssuranceTopologySiteSummariesBodyFilter,
    )
    from ..models.post_v2_assurance_topology_site_summaries_body_time_window import (
        PostV2AssuranceTopologySiteSummariesBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologySiteSummariesBody")


@_attrs_define
class PostV2AssuranceTopologySiteSummariesBody:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        app_server_key (Union[Unset, str]):  Example: TYPE_STRING.
        bucket_id (Union[Unset, str]):  Example: TYPE_ENUM.
        filter_ (Union[Unset, PostV2AssuranceTopologySiteSummariesBodyFilter]):
        time_window (Union[Unset, PostV2AssuranceTopologySiteSummariesBodyTimeWindow]):
    """

    app_name: Union[Unset, str] = UNSET
    app_server_key: Union[Unset, str] = UNSET
    bucket_id: Union[Unset, str] = UNSET
    filter_: Union[Unset, "PostV2AssuranceTopologySiteSummariesBodyFilter"] = UNSET
    time_window: Union[Unset, "PostV2AssuranceTopologySiteSummariesBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        app_server_key = self.app_server_key

        bucket_id = self.bucket_id

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if app_server_key is not UNSET:
            field_dict["appServerKey"] = app_server_key
        if bucket_id is not UNSET:
            field_dict["bucketId"] = bucket_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_site_summaries_body_filter import (
            PostV2AssuranceTopologySiteSummariesBodyFilter,
        )
        from ..models.post_v2_assurance_topology_site_summaries_body_time_window import (
            PostV2AssuranceTopologySiteSummariesBodyTimeWindow,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        app_server_key = d.pop("appServerKey", UNSET)

        bucket_id = d.pop("bucketId", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, PostV2AssuranceTopologySiteSummariesBodyFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostV2AssuranceTopologySiteSummariesBodyFilter.from_dict(_filter_)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceTopologySiteSummariesBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceTopologySiteSummariesBodyTimeWindow.from_dict(_time_window)

        post_v2_assurance_topology_site_summaries_body = cls(
            app_name=app_name,
            app_server_key=app_server_key,
            bucket_id=bucket_id,
            filter_=filter_,
            time_window=time_window,
        )

        post_v2_assurance_topology_site_summaries_body.additional_properties = d
        return post_v2_assurance_topology_site_summaries_body

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
