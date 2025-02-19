from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_id_details_response_200_details_aws_advance_settings import (
        GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings,
    )
    from ..models.get_v1_gateways_id_details_response_200_details_aws_transit_connection import (
        GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection,
    )


T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200DetailsAws")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200DetailsAws:
    """
    Attributes:
        account_id (Union[Unset, str]):  Example: TYPE_STRING.
        advance_settings (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings]):
        transit_connection (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection]):
    """

    account_id: Union[Unset, str] = UNSET
    advance_settings: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings"] = UNSET
    transit_connection: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        advance_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.advance_settings, Unset):
            advance_settings = self.advance_settings.to_dict()

        transit_connection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transit_connection, Unset):
            transit_connection = self.transit_connection.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if advance_settings is not UNSET:
            field_dict["advanceSettings"] = advance_settings
        if transit_connection is not UNSET:
            field_dict["transitConnection"] = transit_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_id_details_response_200_details_aws_advance_settings import (
            GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_aws_transit_connection import (
            GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection,
        )

        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        _advance_settings = d.pop("advanceSettings", UNSET)
        advance_settings: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings]
        if isinstance(_advance_settings, Unset):
            advance_settings = UNSET
        else:
            advance_settings = GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings.from_dict(_advance_settings)

        _transit_connection = d.pop("transitConnection", UNSET)
        transit_connection: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection]
        if isinstance(_transit_connection, Unset):
            transit_connection = UNSET
        else:
            transit_connection = GetV1GatewaysIdDetailsResponse200DetailsAwsTransitConnection.from_dict(
                _transit_connection
            )

        get_v1_gateways_id_details_response_200_details_aws = cls(
            account_id=account_id,
            advance_settings=advance_settings,
            transit_connection=transit_connection,
        )

        get_v1_gateways_id_details_response_200_details_aws.additional_properties = d
        return get_v1_gateways_id_details_response_200_details_aws

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
