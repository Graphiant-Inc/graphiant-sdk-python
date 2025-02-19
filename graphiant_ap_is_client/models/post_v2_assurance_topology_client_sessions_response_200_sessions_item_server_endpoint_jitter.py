from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpointJitter")


@_attrs_define
class PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpointJitter:
    """
    Attributes:
        avg (Union[Unset, str]):  Example: TYPE_FLOAT.
        max_ (Union[Unset, str]):  Example: TYPE_FLOAT.
        min_ (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    avg: Union[Unset, str] = UNSET
    max_: Union[Unset, str] = UNSET
    min_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg = self.avg

        max_ = self.max_

        min_ = self.min_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg is not UNSET:
            field_dict["avg"] = avg
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        avg = d.pop("avg", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_endpoint_jitter = cls(
            avg=avg,
            max_=max_,
            min_=min_,
        )

        post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_endpoint_jitter.additional_properties = d
        return post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_endpoint_jitter

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
