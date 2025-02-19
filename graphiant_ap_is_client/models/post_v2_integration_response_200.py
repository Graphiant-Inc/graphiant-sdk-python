from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_integration_response_200_integration import PostV2IntegrationResponse200Integration


T = TypeVar("T", bound="PostV2IntegrationResponse200")


@_attrs_define
class PostV2IntegrationResponse200:
    """
    Attributes:
        integration (Union[Unset, PostV2IntegrationResponse200Integration]):
    """

    integration: Union[Unset, "PostV2IntegrationResponse200Integration"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integration is not UNSET:
            field_dict["integration"] = integration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_integration_response_200_integration import PostV2IntegrationResponse200Integration

        d = src_dict.copy()
        _integration = d.pop("integration", UNSET)
        integration: Union[Unset, PostV2IntegrationResponse200Integration]
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = PostV2IntegrationResponse200Integration.from_dict(_integration)

        post_v2_integration_response_200 = cls(
            integration=integration,
        )

        post_v2_integration_response_200.additional_properties = d
        return post_v2_integration_response_200

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
