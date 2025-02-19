from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionDetailsResponse200SessionPopLinksItem")


@_attrs_define
class PostV2AssuranceTopologyClientSessionDetailsResponse200SessionPopLinksItem:
    """
    Attributes:
        first_pop_name (Union[Unset, str]):  Example: TYPE_STRING.
        jitter (Union[Unset, str]):  Example: TYPE_FLOAT.
        latency (Union[Unset, str]):  Example: TYPE_FLOAT.
        loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        second_pop_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    first_pop_name: Union[Unset, str] = UNSET
    jitter: Union[Unset, str] = UNSET
    latency: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    second_pop_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_pop_name = self.first_pop_name

        jitter = self.jitter

        latency = self.latency

        loss = self.loss

        second_pop_name = self.second_pop_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_pop_name is not UNSET:
            field_dict["firstPopName"] = first_pop_name
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss
        if second_pop_name is not UNSET:
            field_dict["secondPopName"] = second_pop_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        first_pop_name = d.pop("firstPopName", UNSET)

        jitter = d.pop("jitter", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        second_pop_name = d.pop("secondPopName", UNSET)

        post_v2_assurance_topology_client_session_details_response_200_session_pop_links_item = cls(
            first_pop_name=first_pop_name,
            jitter=jitter,
            latency=latency,
            loss=loss,
            second_pop_name=second_pop_name,
        )

        post_v2_assurance_topology_client_session_details_response_200_session_pop_links_item.additional_properties = d
        return post_v2_assurance_topology_client_session_details_response_200_session_pop_links_item

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
