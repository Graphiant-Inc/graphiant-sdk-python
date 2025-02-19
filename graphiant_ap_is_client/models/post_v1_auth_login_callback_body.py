from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_auth_login_callback_body_relay_state import PostV1AuthLoginCallbackBodyRelayState
    from ..models.post_v1_auth_login_callback_body_saml_response import PostV1AuthLoginCallbackBodySAMLResponse


T = TypeVar("T", bound="PostV1AuthLoginCallbackBody")


@_attrs_define
class PostV1AuthLoginCallbackBody:
    """
    Attributes:
        relay_state (Union[Unset, PostV1AuthLoginCallbackBodyRelayState]):  Example: any.
        saml_response (Union[Unset, PostV1AuthLoginCallbackBodySAMLResponse]):  Example: any.
    """

    relay_state: Union[Unset, "PostV1AuthLoginCallbackBodyRelayState"] = UNSET
    saml_response: Union[Unset, "PostV1AuthLoginCallbackBodySAMLResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relay_state: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relay_state, Unset):
            relay_state = self.relay_state.to_dict()

        saml_response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.saml_response, Unset):
            saml_response = self.saml_response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relay_state is not UNSET:
            field_dict["RelayState"] = relay_state
        if saml_response is not UNSET:
            field_dict["SAMLResponse"] = saml_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_auth_login_callback_body_relay_state import PostV1AuthLoginCallbackBodyRelayState
        from ..models.post_v1_auth_login_callback_body_saml_response import PostV1AuthLoginCallbackBodySAMLResponse

        d = src_dict.copy()
        _relay_state = d.pop("RelayState", UNSET)
        relay_state: Union[Unset, PostV1AuthLoginCallbackBodyRelayState]
        if isinstance(_relay_state, Unset):
            relay_state = UNSET
        else:
            relay_state = PostV1AuthLoginCallbackBodyRelayState.from_dict(_relay_state)

        _saml_response = d.pop("SAMLResponse", UNSET)
        saml_response: Union[Unset, PostV1AuthLoginCallbackBodySAMLResponse]
        if isinstance(_saml_response, Unset):
            saml_response = UNSET
        else:
            saml_response = PostV1AuthLoginCallbackBodySAMLResponse.from_dict(_saml_response)

        post_v1_auth_login_callback_body = cls(
            relay_state=relay_state,
            saml_response=saml_response,
        )

        post_v1_auth_login_callback_body.additional_properties = d
        return post_v1_auth_login_callback_body

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
