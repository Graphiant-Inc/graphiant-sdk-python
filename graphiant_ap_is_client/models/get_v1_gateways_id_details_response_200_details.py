from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_id_details_response_200_details_aws import GetV1GatewaysIdDetailsResponse200DetailsAws
    from ..models.get_v1_gateways_id_details_response_200_details_azure import (
        GetV1GatewaysIdDetailsResponse200DetailsAzure,
    )
    from ..models.get_v1_gateways_id_details_response_200_details_gcp import GetV1GatewaysIdDetailsResponse200DetailsGcp
    from ..models.get_v1_gateways_id_details_response_200_details_ipsec_gateway import (
        GetV1GatewaysIdDetailsResponse200DetailsIpsecGateway,
    )
    from ..models.get_v1_gateways_id_details_response_200_details_oci import GetV1GatewaysIdDetailsResponse200DetailsOci


T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200Details")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200Details:
    """
    Attributes:
        aws (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAws]):
        azure (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAzure]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        gcp (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsGcp]):
        ipsec_gateway (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsIpsecGateway]):
        oci (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsOci]):
        region_id (Union[Unset, str]):  Example: TYPE_INT32.
        speed (Union[Unset, str]):  Example: TYPE_ENUM.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    aws: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsAws"] = UNSET
    azure: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsAzure"] = UNSET
    description: Union[Unset, str] = UNSET
    gcp: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsGcp"] = UNSET
    ipsec_gateway: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsIpsecGateway"] = UNSET
    oci: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsOci"] = UNSET
    region_id: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        azure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        description = self.description

        gcp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()

        ipsec_gateway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipsec_gateway, Unset):
            ipsec_gateway = self.ipsec_gateway.to_dict()

        oci: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oci, Unset):
            oci = self.oci.to_dict()

        region_id = self.region_id

        speed = self.speed

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws is not UNSET:
            field_dict["aws"] = aws
        if azure is not UNSET:
            field_dict["azure"] = azure
        if description is not UNSET:
            field_dict["description"] = description
        if gcp is not UNSET:
            field_dict["gcp"] = gcp
        if ipsec_gateway is not UNSET:
            field_dict["ipsecGateway"] = ipsec_gateway
        if oci is not UNSET:
            field_dict["oci"] = oci
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if speed is not UNSET:
            field_dict["speed"] = speed
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_id_details_response_200_details_aws import (
            GetV1GatewaysIdDetailsResponse200DetailsAws,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_azure import (
            GetV1GatewaysIdDetailsResponse200DetailsAzure,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_gcp import (
            GetV1GatewaysIdDetailsResponse200DetailsGcp,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_ipsec_gateway import (
            GetV1GatewaysIdDetailsResponse200DetailsIpsecGateway,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_oci import (
            GetV1GatewaysIdDetailsResponse200DetailsOci,
        )

        d = src_dict.copy()
        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAws]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = GetV1GatewaysIdDetailsResponse200DetailsAws.from_dict(_aws)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAzure]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = GetV1GatewaysIdDetailsResponse200DetailsAzure.from_dict(_azure)

        description = d.pop("description", UNSET)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsGcp]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = GetV1GatewaysIdDetailsResponse200DetailsGcp.from_dict(_gcp)

        _ipsec_gateway = d.pop("ipsecGateway", UNSET)
        ipsec_gateway: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsIpsecGateway]
        if isinstance(_ipsec_gateway, Unset):
            ipsec_gateway = UNSET
        else:
            ipsec_gateway = GetV1GatewaysIdDetailsResponse200DetailsIpsecGateway.from_dict(_ipsec_gateway)

        _oci = d.pop("oci", UNSET)
        oci: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsOci]
        if isinstance(_oci, Unset):
            oci = UNSET
        else:
            oci = GetV1GatewaysIdDetailsResponse200DetailsOci.from_dict(_oci)

        region_id = d.pop("regionId", UNSET)

        speed = d.pop("speed", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        get_v1_gateways_id_details_response_200_details = cls(
            aws=aws,
            azure=azure,
            description=description,
            gcp=gcp,
            ipsec_gateway=ipsec_gateway,
            oci=oci,
            region_id=region_id,
            speed=speed,
            vrf_id=vrf_id,
        )

        get_v1_gateways_id_details_response_200_details.additional_properties = d
        return get_v1_gateways_id_details_response_200_details

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
