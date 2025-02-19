from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_body_policy import PostV1ExtranetsB2BBodyPolicy


T = TypeVar("T", bound="PostV1ExtranetsB2BBody")


@_attrs_define
class PostV1ExtranetsB2BBody:
    """
    Attributes:
        policy (Union[Unset, PostV1ExtranetsB2BBodyPolicy]):
        service_name (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    policy: Union[Unset, "PostV1ExtranetsB2BBodyPolicy"] = UNSET
    service_name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        service_name = self.service_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_body_policy import PostV1ExtranetsB2BBodyPolicy

        d = src_dict.copy()
        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, PostV1ExtranetsB2BBodyPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PostV1ExtranetsB2BBodyPolicy.from_dict(_policy)

        service_name = d.pop("serviceName", UNSET)

        type_ = d.pop("type", UNSET)

        post_v1_extranets_b2b_body = cls(
            policy=policy,
            service_name=service_name,
            type_=type_,
        )

        post_v1_extranets_b2b_body.additional_properties = d
        return post_v1_extranets_b2b_body

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
