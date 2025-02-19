from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceFlowSummaryResponse200ServerEndpointEdgesItem")


@_attrs_define
class PostV2AssuranceFlowSummaryResponse200ServerEndpointEdgesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        post_v2_assurance_flow_summary_response_200_server_endpoint_edges_item = cls(
            device_id=device_id,
            device_name=device_name,
        )

        post_v2_assurance_flow_summary_response_200_server_endpoint_edges_item.additional_properties = d
        return post_v2_assurance_flow_summary_response_200_server_endpoint_edges_item

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
