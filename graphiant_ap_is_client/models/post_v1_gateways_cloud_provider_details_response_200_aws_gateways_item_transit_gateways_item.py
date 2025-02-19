from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item import (
        PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem,
    )


T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItem:
    """
    Attributes:
        asn (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_STRING.
        vpcs (Union[Unset,
            list['PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem']]):
    """

    asn: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    vpcs: Union[
        Unset, list["PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asn = self.asn

        id = self.id

        vpcs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vpcs, Unset):
            vpcs = []
            for vpcs_item_data in self.vpcs:
                vpcs_item = vpcs_item_data.to_dict()
                vpcs.append(vpcs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asn is not UNSET:
            field_dict["asn"] = asn
        if id is not UNSET:
            field_dict["id"] = id
        if vpcs is not UNSET:
            field_dict["vpcs"] = vpcs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item import (
            PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem,
        )

        d = src_dict.copy()
        asn = d.pop("asn", UNSET)

        id = d.pop("id", UNSET)

        vpcs = []
        _vpcs = d.pop("vpcs", UNSET)
        for vpcs_item_data in _vpcs or []:
            vpcs_item = (
                PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem.from_dict(
                    vpcs_item_data
                )
            )

            vpcs.append(vpcs_item)

        post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item = cls(
            asn=asn,
            id=id,
            vpcs=vpcs,
        )

        post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item.additional_properties = d
        return post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item

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
