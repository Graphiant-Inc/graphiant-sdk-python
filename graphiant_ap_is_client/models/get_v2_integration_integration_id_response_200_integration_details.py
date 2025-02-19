from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV2IntegrationIntegrationIdResponse200IntegrationDetails")


@_attrs_define
class GetV2IntegrationIntegrationIdResponse200IntegrationDetails:
    """
    Attributes:
        opsgenie_key (Union[Unset, str]):  Example: TYPE_STRING.
        opsramp_details (Union[Unset, str]):  Example: TYPE_STRING.
        webhook_url (Union[Unset, str]):  Example: TYPE_STRING.
    """

    opsgenie_key: Union[Unset, str] = UNSET
    opsramp_details: Union[Unset, str] = UNSET
    webhook_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opsgenie_key = self.opsgenie_key

        opsramp_details = self.opsramp_details

        webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opsgenie_key is not UNSET:
            field_dict["opsgenieKey"] = opsgenie_key
        if opsramp_details is not UNSET:
            field_dict["opsrampDetails"] = opsramp_details
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        opsgenie_key = d.pop("opsgenieKey", UNSET)

        opsramp_details = d.pop("opsrampDetails", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        get_v2_integration_integration_id_response_200_integration_details = cls(
            opsgenie_key=opsgenie_key,
            opsramp_details=opsramp_details,
            webhook_url=webhook_url,
        )

        get_v2_integration_integration_id_response_200_integration_details.additional_properties = d
        return get_v2_integration_integration_id_response_200_integration_details

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
