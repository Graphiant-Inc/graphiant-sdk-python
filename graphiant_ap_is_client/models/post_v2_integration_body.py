from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_integration_body_integration_body import PostV2IntegrationBodyIntegrationBody


T = TypeVar("T", bound="PostV2IntegrationBody")


@_attrs_define
class PostV2IntegrationBody:
    """
    Attributes:
        integration_body (Union[Unset, PostV2IntegrationBodyIntegrationBody]):
    """

    integration_body: Union[Unset, "PostV2IntegrationBodyIntegrationBody"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.integration_body, Unset):
            integration_body = self.integration_body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integration_body is not UNSET:
            field_dict["integrationBody"] = integration_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_integration_body_integration_body import PostV2IntegrationBodyIntegrationBody

        d = src_dict.copy()
        _integration_body = d.pop("integrationBody", UNSET)
        integration_body: Union[Unset, PostV2IntegrationBodyIntegrationBody]
        if isinstance(_integration_body, Unset):
            integration_body = UNSET
        else:
            integration_body = PostV2IntegrationBodyIntegrationBody.from_dict(_integration_body)

        post_v2_integration_body = cls(
            integration_body=integration_body,
        )

        post_v2_integration_body.additional_properties = d
        return post_v2_integration_body

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
