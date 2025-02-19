from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_auth_mfa_body_code import PostV1AuthMfaBodyCode
    from ..models.post_v1_auth_mfa_body_email import PostV1AuthMfaBodyEmail
    from ..models.post_v1_auth_mfa_body_mfa_type import PostV1AuthMfaBodyMfaType
    from ..models.post_v1_auth_mfa_body_state_token import PostV1AuthMfaBodyStateToken


T = TypeVar("T", bound="PostV1AuthMfaBody")


@_attrs_define
class PostV1AuthMfaBody:
    """
    Attributes:
        email (Union[Unset, PostV1AuthMfaBodyEmail]):  Example: any.
        mfa_type (Union[Unset, PostV1AuthMfaBodyMfaType]):  Example: any.
        code (Union[Unset, PostV1AuthMfaBodyCode]):  Example: any.
        state_token (Union[Unset, PostV1AuthMfaBodyStateToken]):  Example: any.
    """

    email: Union[Unset, "PostV1AuthMfaBodyEmail"] = UNSET
    mfa_type: Union[Unset, "PostV1AuthMfaBodyMfaType"] = UNSET
    code: Union[Unset, "PostV1AuthMfaBodyCode"] = UNSET
    state_token: Union[Unset, "PostV1AuthMfaBodyStateToken"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        mfa_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mfa_type, Unset):
            mfa_type = self.mfa_type.to_dict()

        code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        state_token: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.state_token, Unset):
            state_token = self.state_token.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if mfa_type is not UNSET:
            field_dict["mfaType"] = mfa_type
        if code is not UNSET:
            field_dict["code"] = code
        if state_token is not UNSET:
            field_dict["stateToken"] = state_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_auth_mfa_body_code import PostV1AuthMfaBodyCode
        from ..models.post_v1_auth_mfa_body_email import PostV1AuthMfaBodyEmail
        from ..models.post_v1_auth_mfa_body_mfa_type import PostV1AuthMfaBodyMfaType
        from ..models.post_v1_auth_mfa_body_state_token import PostV1AuthMfaBodyStateToken

        d = src_dict.copy()
        _email = d.pop("email", UNSET)
        email: Union[Unset, PostV1AuthMfaBodyEmail]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = PostV1AuthMfaBodyEmail.from_dict(_email)

        _mfa_type = d.pop("mfaType", UNSET)
        mfa_type: Union[Unset, PostV1AuthMfaBodyMfaType]
        if isinstance(_mfa_type, Unset):
            mfa_type = UNSET
        else:
            mfa_type = PostV1AuthMfaBodyMfaType.from_dict(_mfa_type)

        _code = d.pop("code", UNSET)
        code: Union[Unset, PostV1AuthMfaBodyCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = PostV1AuthMfaBodyCode.from_dict(_code)

        _state_token = d.pop("stateToken", UNSET)
        state_token: Union[Unset, PostV1AuthMfaBodyStateToken]
        if isinstance(_state_token, Unset):
            state_token = UNSET
        else:
            state_token = PostV1AuthMfaBodyStateToken.from_dict(_state_token)

        post_v1_auth_mfa_body = cls(
            email=email,
            mfa_type=mfa_type,
            code=code,
            state_token=state_token,
        )

        post_v1_auth_mfa_body.additional_properties = d
        return post_v1_auth_mfa_body

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
