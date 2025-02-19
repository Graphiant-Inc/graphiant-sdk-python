from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_extranets_b2b_id_body_policy import PutV1ExtranetsB2BIdBodyPolicy


T = TypeVar("T", bound="PutV1ExtranetsB2BIdBody")


@_attrs_define
class PutV1ExtranetsB2BIdBody:
    """
    Attributes:
        policy (Union[Unset, PutV1ExtranetsB2BIdBodyPolicy]):
    """

    policy: Union[Unset, "PutV1ExtranetsB2BIdBodyPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_extranets_b2b_id_body_policy import PutV1ExtranetsB2BIdBodyPolicy

        d = src_dict.copy()
        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, PutV1ExtranetsB2BIdBodyPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PutV1ExtranetsB2BIdBodyPolicy.from_dict(_policy)

        put_v1_extranets_b2b_id_body = cls(
            policy=policy,
        )

        put_v1_extranets_b2b_id_body.additional_properties = d
        return put_v1_extranets_b2b_id_body

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
