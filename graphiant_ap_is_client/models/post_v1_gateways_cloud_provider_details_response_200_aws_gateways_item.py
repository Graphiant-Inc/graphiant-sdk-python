from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item import (
        PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem,
    )


T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem:
    """
    Attributes:
        asn (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_STRING.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        transit_gateways (Union[Unset,
            list['PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem']]):
    """

    asn: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    transit_gateways: Union[
        Unset, list["PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asn = self.asn

        id = self.id

        name = self.name

        transit_gateways: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transit_gateways, Unset):
            transit_gateways = []
            for transit_gateways_item_data in self.transit_gateways:
                transit_gateways_item = transit_gateways_item_data.to_dict()
                transit_gateways.append(transit_gateways_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asn is not UNSET:
            field_dict["asn"] = asn
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if transit_gateways is not UNSET:
            field_dict["transitGateways"] = transit_gateways

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item import (
            PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem,
        )

        d = src_dict.copy()
        asn = d.pop("asn", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        transit_gateways = []
        _transit_gateways = d.pop("transitGateways", UNSET)
        for transit_gateways_item_data in _transit_gateways or []:
            transit_gateways_item = (
                PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem.from_dict(
                    transit_gateways_item_data
                )
            )

            transit_gateways.append(transit_gateways_item)

        post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item = cls(
            asn=asn,
            id=id,
            name=name,
            transit_gateways=transit_gateways,
        )

        post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item.additional_properties = d
        return post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item

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
