from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1ExtranetsB2BConsumerIdStatusBody")


@_attrs_define
class PutV1ExtranetsB2BConsumerIdStatusBody:
    """
    Attributes:
        cid (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    cid: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cid = self.cid

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cid is not UNSET:
            field_dict["cid"] = cid
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cid = d.pop("cid", UNSET)

        status = d.pop("status", UNSET)

        put_v1_extranets_b2b_consumer_id_status_body = cls(
            cid=cid,
            status=status,
        )

        put_v1_extranets_b2b_consumer_id_status_body.additional_properties = d
        return put_v1_extranets_b2b_consumer_id_status_body

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
