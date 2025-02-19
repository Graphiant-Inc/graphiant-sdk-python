from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_body_filter_item import PostV1FlowsBodyFilterItem
    from ..models.post_v1_flows_body_old_ts import PostV1FlowsBodyOldTs
    from ..models.post_v1_flows_body_recent_ts import PostV1FlowsBodyRecentTs


T = TypeVar("T", bound="PostV1FlowsBody")


@_attrs_define
class PostV1FlowsBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        filter_ (Union[Unset, list['PostV1FlowsBodyFilterItem']]):
        nr_flows (Union[Unset, str]):  Example: 22.
        old_ts (Union[Unset, PostV1FlowsBodyOldTs]):
        recent_ts (Union[Unset, PostV1FlowsBodyRecentTs]):
    """

    device_id: Union[Unset, str] = UNSET
    filter_: Union[Unset, list["PostV1FlowsBodyFilterItem"]] = UNSET
    nr_flows: Union[Unset, str] = UNSET
    old_ts: Union[Unset, "PostV1FlowsBodyOldTs"] = UNSET
    recent_ts: Union[Unset, "PostV1FlowsBodyRecentTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        filter_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        nr_flows = self.nr_flows

        old_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.old_ts, Unset):
            old_ts = self.old_ts.to_dict()

        recent_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recent_ts, Unset):
            recent_ts = self.recent_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if nr_flows is not UNSET:
            field_dict["nrFlows"] = nr_flows
        if old_ts is not UNSET:
            field_dict["oldTs"] = old_ts
        if recent_ts is not UNSET:
            field_dict["recentTs"] = recent_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_body_filter_item import PostV1FlowsBodyFilterItem
        from ..models.post_v1_flows_body_old_ts import PostV1FlowsBodyOldTs
        from ..models.post_v1_flows_body_recent_ts import PostV1FlowsBodyRecentTs

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = PostV1FlowsBodyFilterItem.from_dict(filter_item_data)

            filter_.append(filter_item)

        nr_flows = d.pop("nrFlows", UNSET)

        _old_ts = d.pop("oldTs", UNSET)
        old_ts: Union[Unset, PostV1FlowsBodyOldTs]
        if isinstance(_old_ts, Unset):
            old_ts = UNSET
        else:
            old_ts = PostV1FlowsBodyOldTs.from_dict(_old_ts)

        _recent_ts = d.pop("recentTs", UNSET)
        recent_ts: Union[Unset, PostV1FlowsBodyRecentTs]
        if isinstance(_recent_ts, Unset):
            recent_ts = UNSET
        else:
            recent_ts = PostV1FlowsBodyRecentTs.from_dict(_recent_ts)

        post_v1_flows_body = cls(
            device_id=device_id,
            filter_=filter_,
            nr_flows=nr_flows,
            old_ts=old_ts,
            recent_ts=recent_ts,
        )

        post_v1_flows_body.additional_properties = d
        return post_v1_flows_body

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
