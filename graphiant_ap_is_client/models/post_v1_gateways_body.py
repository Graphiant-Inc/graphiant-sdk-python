from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_body_details import PostV1GatewaysBodyDetails


T = TypeVar("T", bound="PostV1GatewaysBody")


@_attrs_define
class PostV1GatewaysBody:
    """
    Attributes:
        details (Union[Unset, PostV1GatewaysBodyDetails]):
    """

    details: Union[Unset, "PostV1GatewaysBodyDetails"] = UNSET
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
        from ..models.post_v1_gateways_body_details import PostV1GatewaysBodyDetails

        d = src_dict.copy()
        _details = d.pop("details", UNSET)
        details: Union[Unset, PostV1GatewaysBodyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PostV1GatewaysBodyDetails.from_dict(_details)

        post_v1_gateways_body = cls(
            details=details,
        )

        post_v1_gateways_body.additional_properties = d
        return post_v1_gateways_body

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
