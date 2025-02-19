from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_auth_login_spa_body_idp import PostV1AuthLoginSpaBodyIdp
    from ..models.post_v1_auth_login_spa_body_user import PostV1AuthLoginSpaBodyUser


T = TypeVar("T", bound="PostV1AuthLoginSpaBody")


@_attrs_define
class PostV1AuthLoginSpaBody:
    """
    Attributes:
        idp (Union[Unset, PostV1AuthLoginSpaBodyIdp]):  Example: any.
        user (Union[Unset, PostV1AuthLoginSpaBodyUser]):  Example: any.
    """

    idp: Union[Unset, "PostV1AuthLoginSpaBodyIdp"] = UNSET
    user: Union[Unset, "PostV1AuthLoginSpaBodyUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.idp, Unset):
            idp = self.idp.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idp is not UNSET:
            field_dict["idp"] = idp
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_auth_login_spa_body_idp import PostV1AuthLoginSpaBodyIdp
        from ..models.post_v1_auth_login_spa_body_user import PostV1AuthLoginSpaBodyUser

        d = src_dict.copy()
        _idp = d.pop("idp", UNSET)
        idp: Union[Unset, PostV1AuthLoginSpaBodyIdp]
        if isinstance(_idp, Unset):
            idp = UNSET
        else:
            idp = PostV1AuthLoginSpaBodyIdp.from_dict(_idp)

        _user = d.pop("user", UNSET)
        user: Union[Unset, PostV1AuthLoginSpaBodyUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PostV1AuthLoginSpaBodyUser.from_dict(_user)

        post_v1_auth_login_spa_body = cls(
            idp=idp,
            user=user,
        )

        post_v1_auth_login_spa_body.additional_properties = d
        return post_v1_auth_login_spa_body

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
