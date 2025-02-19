from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_sites_site_id_circuits_response_200_data_item_circuits_item import (
        GetV1SitesSiteIdCircuitsResponse200DataItemCircuitsItem,
    )


T = TypeVar("T", bound="GetV1SitesSiteIdCircuitsResponse200DataItem")


@_attrs_define
class GetV1SitesSiteIdCircuitsResponse200DataItem:
    """
    Attributes:
        circuits (Union[Unset, list['GetV1SitesSiteIdCircuitsResponse200DataItemCircuitsItem']]):
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    circuits: Union[Unset, list["GetV1SitesSiteIdCircuitsResponse200DataItemCircuitsItem"]] = UNSET
    device_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = []
            for circuits_item_data in self.circuits:
                circuits_item = circuits_item_data.to_dict()
                circuits.append(circuits_item)

        device_id = self.device_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuits is not UNSET:
            field_dict["circuits"] = circuits
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_sites_site_id_circuits_response_200_data_item_circuits_item import (
            GetV1SitesSiteIdCircuitsResponse200DataItemCircuitsItem,
        )

        d = src_dict.copy()
        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = GetV1SitesSiteIdCircuitsResponse200DataItemCircuitsItem.from_dict(circuits_item_data)

            circuits.append(circuits_item)

        device_id = d.pop("deviceId", UNSET)

        get_v1_sites_site_id_circuits_response_200_data_item = cls(
            circuits=circuits,
            device_id=device_id,
        )

        get_v1_sites_site_id_circuits_response_200_data_item.additional_properties = d
        return get_v1_sites_site_id_circuits_response_200_data_item

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
