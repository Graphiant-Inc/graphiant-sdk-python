from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_body_details_aws import PostV1GatewaysBodyDetailsAws
    from ..models.post_v1_gateways_body_details_azure import PostV1GatewaysBodyDetailsAzure
    from ..models.post_v1_gateways_body_details_gcp import PostV1GatewaysBodyDetailsGcp
    from ..models.post_v1_gateways_body_details_ipsec_gateway import PostV1GatewaysBodyDetailsIpsecGateway
    from ..models.post_v1_gateways_body_details_oci import PostV1GatewaysBodyDetailsOci


T = TypeVar("T", bound="PostV1GatewaysBodyDetails")


@_attrs_define
class PostV1GatewaysBodyDetails:
    """
    Attributes:
        aws (Union[Unset, PostV1GatewaysBodyDetailsAws]):
        azure (Union[Unset, PostV1GatewaysBodyDetailsAzure]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        gcp (Union[Unset, PostV1GatewaysBodyDetailsGcp]):
        ipsec_gateway (Union[Unset, PostV1GatewaysBodyDetailsIpsecGateway]):
        oci (Union[Unset, PostV1GatewaysBodyDetailsOci]):
        region_id (Union[Unset, str]):  Example: TYPE_INT32.
        speed (Union[Unset, str]):  Example: TYPE_ENUM.
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    aws: Union[Unset, "PostV1GatewaysBodyDetailsAws"] = UNSET
    azure: Union[Unset, "PostV1GatewaysBodyDetailsAzure"] = UNSET
    description: Union[Unset, str] = UNSET
    gcp: Union[Unset, "PostV1GatewaysBodyDetailsGcp"] = UNSET
    ipsec_gateway: Union[Unset, "PostV1GatewaysBodyDetailsIpsecGateway"] = UNSET
    oci: Union[Unset, "PostV1GatewaysBodyDetailsOci"] = UNSET
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
        from ..models.post_v1_gateways_body_details_aws import PostV1GatewaysBodyDetailsAws
        from ..models.post_v1_gateways_body_details_azure import PostV1GatewaysBodyDetailsAzure
        from ..models.post_v1_gateways_body_details_gcp import PostV1GatewaysBodyDetailsGcp
        from ..models.post_v1_gateways_body_details_ipsec_gateway import PostV1GatewaysBodyDetailsIpsecGateway
        from ..models.post_v1_gateways_body_details_oci import PostV1GatewaysBodyDetailsOci

        d = src_dict.copy()
        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, PostV1GatewaysBodyDetailsAws]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = PostV1GatewaysBodyDetailsAws.from_dict(_aws)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, PostV1GatewaysBodyDetailsAzure]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = PostV1GatewaysBodyDetailsAzure.from_dict(_azure)

        description = d.pop("description", UNSET)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, PostV1GatewaysBodyDetailsGcp]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = PostV1GatewaysBodyDetailsGcp.from_dict(_gcp)

        _ipsec_gateway = d.pop("ipsecGateway", UNSET)
        ipsec_gateway: Union[Unset, PostV1GatewaysBodyDetailsIpsecGateway]
        if isinstance(_ipsec_gateway, Unset):
            ipsec_gateway = UNSET
        else:
            ipsec_gateway = PostV1GatewaysBodyDetailsIpsecGateway.from_dict(_ipsec_gateway)

        _oci = d.pop("oci", UNSET)
        oci: Union[Unset, PostV1GatewaysBodyDetailsOci]
        if isinstance(_oci, Unset):
            oci = UNSET
        else:
            oci = PostV1GatewaysBodyDetailsOci.from_dict(_oci)

        region_id = d.pop("regionId", UNSET)

        speed = d.pop("speed", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        post_v1_gateways_body_details = cls(
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

        post_v1_gateways_body_details.additional_properties = d
        return post_v1_gateways_body_details

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
