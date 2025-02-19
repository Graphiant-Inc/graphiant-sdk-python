from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200DetailsOci")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200DetailsOci:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        fast_connect_ocid (Union[Unset, str]):  Example: TYPE_STRING.
        routing_policy (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    fast_connect_ocid: Union[Unset, str] = UNSET
    routing_policy: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        fast_connect_ocid = self.fast_connect_ocid

        routing_policy = self.routing_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if fast_connect_ocid is not UNSET:
            field_dict["fastConnectOcid"] = fast_connect_ocid
        if routing_policy is not UNSET:
            field_dict["routingPolicy"] = routing_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        fast_connect_ocid = d.pop("fastConnectOcid", UNSET)

        routing_policy = d.pop("routingPolicy", UNSET)

        get_v1_gateways_id_details_response_200_details_oci = cls(
            description=description,
            fast_connect_ocid=fast_connect_ocid,
            routing_policy=routing_policy,
        )

        get_v1_gateways_id_details_response_200_details_oci.additional_properties = d
        return get_v1_gateways_id_details_response_200_details_oci

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
