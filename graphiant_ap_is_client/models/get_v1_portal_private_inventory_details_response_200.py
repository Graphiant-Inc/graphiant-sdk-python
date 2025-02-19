from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_portal_private_inventory_details_response_200_details_item import (
        GetV1PortalPrivateInventoryDetailsResponse200DetailsItem,
    )


T = TypeVar("T", bound="GetV1PortalPrivateInventoryDetailsResponse200")


@_attrs_define
class GetV1PortalPrivateInventoryDetailsResponse200:
    """
    Attributes:
        details (Union[Unset, list['GetV1PortalPrivateInventoryDetailsResponse200DetailsItem']]):
    """

    details: Union[Unset, list["GetV1PortalPrivateInventoryDetailsResponse200DetailsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_portal_private_inventory_details_response_200_details_item import (
            GetV1PortalPrivateInventoryDetailsResponse200DetailsItem,
        )

        d = src_dict.copy()
        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = GetV1PortalPrivateInventoryDetailsResponse200DetailsItem.from_dict(details_item_data)

            details.append(details_item)

        get_v1_portal_private_inventory_details_response_200 = cls(
            details=details,
        )

        get_v1_portal_private_inventory_details_response_200.additional_properties = d
        return get_v1_portal_private_inventory_details_response_200

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
