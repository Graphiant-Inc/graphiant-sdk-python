from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_auth_login_body_password import PostV1AuthLoginBodyPassword
    from ..models.post_v1_auth_login_body_username import PostV1AuthLoginBodyUsername


T = TypeVar("T", bound="PostV1AuthLoginBody")


@_attrs_define
class PostV1AuthLoginBody:
    """
    Attributes:
        username (Union[Unset, PostV1AuthLoginBodyUsername]):  Example: any.
        password (Union[Unset, PostV1AuthLoginBodyPassword]):  Example: any.
    """

    username: Union[Unset, "PostV1AuthLoginBodyUsername"] = UNSET
    password: Union[Unset, "PostV1AuthLoginBodyPassword"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.username, Unset):
            username = self.username.to_dict()

        password: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_auth_login_body_password import PostV1AuthLoginBodyPassword
        from ..models.post_v1_auth_login_body_username import PostV1AuthLoginBodyUsername

        d = src_dict.copy()
        _username = d.pop("username", UNSET)
        username: Union[Unset, PostV1AuthLoginBodyUsername]
        if isinstance(_username, Unset):
            username = UNSET
        else:
            username = PostV1AuthLoginBodyUsername.from_dict(_username)

        _password = d.pop("password", UNSET)
        password: Union[Unset, PostV1AuthLoginBodyPassword]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = PostV1AuthLoginBodyPassword.from_dict(_password)

        post_v1_auth_login_body = cls(
            username=username,
            password=password,
        )

        post_v1_auth_login_body.additional_properties = d
        return post_v1_auth_login_body

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
