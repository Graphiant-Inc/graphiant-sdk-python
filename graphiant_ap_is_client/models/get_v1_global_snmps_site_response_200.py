from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_snmps_site_response_200_snmps_item import GetV1GlobalSnmpsSiteResponse200SnmpsItem


T = TypeVar("T", bound="GetV1GlobalSnmpsSiteResponse200")


@_attrs_define
class GetV1GlobalSnmpsSiteResponse200:
    """
    Attributes:
        snmps (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItem']]):
    """

    snmps: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snmps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snmps, Unset):
            snmps = []
            for snmps_item_data in self.snmps:
                snmps_item = snmps_item_data.to_dict()
                snmps.append(snmps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snmps is not UNSET:
            field_dict["snmps"] = snmps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_snmps_site_response_200_snmps_item import GetV1GlobalSnmpsSiteResponse200SnmpsItem

        d = src_dict.copy()
        snmps = []
        _snmps = d.pop("snmps", UNSET)
        for snmps_item_data in _snmps or []:
            snmps_item = GetV1GlobalSnmpsSiteResponse200SnmpsItem.from_dict(snmps_item_data)

            snmps.append(snmps_item)

        get_v1_global_snmps_site_response_200 = cls(
            snmps=snmps,
        )

        get_v1_global_snmps_site_response_200.additional_properties = d
        return get_v1_global_snmps_site_response_200

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
