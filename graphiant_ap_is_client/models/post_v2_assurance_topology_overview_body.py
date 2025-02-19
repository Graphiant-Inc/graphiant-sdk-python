from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_overview_body_filter import PostV2AssuranceTopologyOverviewBodyFilter
    from ..models.post_v2_assurance_topology_overview_body_slider_time_window import (
        PostV2AssuranceTopologyOverviewBodySliderTimeWindow,
    )
    from ..models.post_v2_assurance_topology_overview_body_time_window import (
        PostV2AssuranceTopologyOverviewBodyTimeWindow,
    )
    from ..models.post_v2_assurance_topology_overview_body_topology_ts import (
        PostV2AssuranceTopologyOverviewBodyTopologyTs,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewBody")


@_attrs_define
class PostV2AssuranceTopologyOverviewBody:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        app_server_key (Union[Unset, str]):  Example: TYPE_STRING.
        bucket_id (Union[Unset, str]):  Example: TYPE_ENUM.
        filter_ (Union[Unset, PostV2AssuranceTopologyOverviewBodyFilter]):
        slider_time_window (Union[Unset, PostV2AssuranceTopologyOverviewBodySliderTimeWindow]):
        time_window (Union[Unset, PostV2AssuranceTopologyOverviewBodyTimeWindow]):
        topology_ts (Union[Unset, PostV2AssuranceTopologyOverviewBodyTopologyTs]):
        topology_type (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    app_name: Union[Unset, str] = UNSET
    app_server_key: Union[Unset, str] = UNSET
    bucket_id: Union[Unset, str] = UNSET
    filter_: Union[Unset, "PostV2AssuranceTopologyOverviewBodyFilter"] = UNSET
    slider_time_window: Union[Unset, "PostV2AssuranceTopologyOverviewBodySliderTimeWindow"] = UNSET
    time_window: Union[Unset, "PostV2AssuranceTopologyOverviewBodyTimeWindow"] = UNSET
    topology_ts: Union[Unset, "PostV2AssuranceTopologyOverviewBodyTopologyTs"] = UNSET
    topology_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        app_server_key = self.app_server_key

        bucket_id = self.bucket_id

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        slider_time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.slider_time_window, Unset):
            slider_time_window = self.slider_time_window.to_dict()

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        topology_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topology_ts, Unset):
            topology_ts = self.topology_ts.to_dict()

        topology_type = self.topology_type

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
        if slider_time_window is not UNSET:
            field_dict["sliderTimeWindow"] = slider_time_window
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window
        if topology_ts is not UNSET:
            field_dict["topologyTs"] = topology_ts
        if topology_type is not UNSET:
            field_dict["topologyType"] = topology_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_overview_body_filter import PostV2AssuranceTopologyOverviewBodyFilter
        from ..models.post_v2_assurance_topology_overview_body_slider_time_window import (
            PostV2AssuranceTopologyOverviewBodySliderTimeWindow,
        )
        from ..models.post_v2_assurance_topology_overview_body_time_window import (
            PostV2AssuranceTopologyOverviewBodyTimeWindow,
        )
        from ..models.post_v2_assurance_topology_overview_body_topology_ts import (
            PostV2AssuranceTopologyOverviewBodyTopologyTs,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        app_server_key = d.pop("appServerKey", UNSET)

        bucket_id = d.pop("bucketId", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, PostV2AssuranceTopologyOverviewBodyFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostV2AssuranceTopologyOverviewBodyFilter.from_dict(_filter_)

        _slider_time_window = d.pop("sliderTimeWindow", UNSET)
        slider_time_window: Union[Unset, PostV2AssuranceTopologyOverviewBodySliderTimeWindow]
        if isinstance(_slider_time_window, Unset):
            slider_time_window = UNSET
        else:
            slider_time_window = PostV2AssuranceTopologyOverviewBodySliderTimeWindow.from_dict(_slider_time_window)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceTopologyOverviewBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceTopologyOverviewBodyTimeWindow.from_dict(_time_window)

        _topology_ts = d.pop("topologyTs", UNSET)
        topology_ts: Union[Unset, PostV2AssuranceTopologyOverviewBodyTopologyTs]
        if isinstance(_topology_ts, Unset):
            topology_ts = UNSET
        else:
            topology_ts = PostV2AssuranceTopologyOverviewBodyTopologyTs.from_dict(_topology_ts)

        topology_type = d.pop("topologyType", UNSET)

        post_v2_assurance_topology_overview_body = cls(
            app_name=app_name,
            app_server_key=app_server_key,
            bucket_id=bucket_id,
            filter_=filter_,
            slider_time_window=slider_time_window,
            time_window=time_window,
            topology_ts=topology_ts,
            topology_type=topology_type,
        )

        post_v2_assurance_topology_overview_body.additional_properties = d
        return post_v2_assurance_topology_overview_body

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
