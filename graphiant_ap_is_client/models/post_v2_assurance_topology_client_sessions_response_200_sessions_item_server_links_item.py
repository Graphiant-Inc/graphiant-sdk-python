from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem")


@_attrs_define
class PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem:
    """
    Attributes:
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        jitter (Union[Unset, str]):  Example: TYPE_FLOAT.
        latency (Union[Unset, str]):  Example: TYPE_FLOAT.
        loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        pop_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    circuit_name: Union[Unset, str] = UNSET
    jitter: Union[Unset, str] = UNSET
    latency: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    pop_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name = self.circuit_name

        jitter = self.jitter

        latency = self.latency

        loss = self.loss

        pop_name = self.pop_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss
        if pop_name is not UNSET:
            field_dict["popName"] = pop_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_name = d.pop("circuitName", UNSET)

        jitter = d.pop("jitter", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        pop_name = d.pop("popName", UNSET)

        post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_links_item = cls(
            circuit_name=circuit_name,
            jitter=jitter,
            latency=latency,
            loss=loss,
            pop_name=pop_name,
        )

        post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_links_item.additional_properties = d
        return post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_links_item

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
