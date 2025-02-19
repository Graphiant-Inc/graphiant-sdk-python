from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_id_details_response_200_details_aws_transit_connection_credentials import (
        GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionCredentials,
    )
    from ..models.get_v1_gateways_id_details_response_200_details_aws_transit_connection_gateway import (
        GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionGateway,
    )


T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection:
    """
    Attributes:
        credentials (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionCredentials]):
        customer_asn (Union[Unset, str]):  Example: TYPE_UINT32.
        gateway (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionGateway]):
        region (Union[Unset, str]):  Example: TYPE_STRING.
    """

    credentials: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionCredentials"] = UNSET
    customer_asn: Union[Unset, str] = UNSET
    gateway: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionGateway"] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        customer_asn = self.customer_asn

        gateway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.to_dict()

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if customer_asn is not UNSET:
            field_dict["customerAsn"] = customer_asn
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_id_details_response_200_details_aws_transit_connection_credentials import (
            GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionCredentials,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_aws_transit_connection_gateway import (
            GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionGateway,
        )

        d = src_dict.copy()
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionCredentials.from_dict(
                _credentials
            )

        customer_asn = d.pop("customerAsn", UNSET)

        _gateway = d.pop("gateway", UNSET)
        gateway: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionGateway]
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnectionGateway.from_dict(_gateway)

        region = d.pop("region", UNSET)

        get_v1_gateways_id_details_response_200_details_aws_transit_connection = cls(
            credentials=credentials,
            customer_asn=customer_asn,
            gateway=gateway,
            region=region,
        )

        get_v1_gateways_id_details_response_200_details_aws_transit_connection.additional_properties = d
        return get_v1_gateways_id_details_response_200_details_aws_transit_connection

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
