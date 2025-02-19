from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_id_details_response_200_details import GetV1GatewaysIdDetailsResponse200Details


T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200:
    """
    Attributes:
        details (Union[Unset, GetV1GatewaysIdDetailsResponse200Details]):
    """

    details: Union[Unset, "GetV1GatewaysIdDetailsResponse200Details"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_id_details_response_200_details import GetV1GatewaysIdDetailsResponse200Details

        d = src_dict.copy()
        _details = d.pop("details", UNSET)
        details: Union[Unset, GetV1GatewaysIdDetailsResponse200Details]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GetV1GatewaysIdDetailsResponse200Details.from_dict(_details)

        get_v1_gateways_id_details_response_200 = cls(
            details=details,
        )

        get_v1_gateways_id_details_response_200.additional_properties = d
        return get_v1_gateways_id_details_response_200

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
