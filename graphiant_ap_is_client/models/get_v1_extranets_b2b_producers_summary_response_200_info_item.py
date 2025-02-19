from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_producers_summary_response_200_info_item_created_at import (
        GetV1ExtranetsB2BProducersSummaryResponse200InfoItemCreatedAt,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BProducersSummaryResponse200InfoItem")


@_attrs_define
class GetV1ExtranetsB2BProducersSummaryResponse200InfoItem:
    """
    Attributes:
        created_at (Union[Unset, GetV1ExtranetsB2BProducersSummaryResponse200InfoItemCreatedAt]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        server_ip_address (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        total_customers (Union[Unset, str]):  Example: TYPE_UINT32.
        total_sites (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    created_at: Union[Unset, "GetV1ExtranetsB2BProducersSummaryResponse200InfoItemCreatedAt"] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    server_ip_address: Union[Unset, list[str]] = UNSET
    status: Union[Unset, str] = UNSET
    total_customers: Union[Unset, str] = UNSET
    total_sites: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        id = self.id

        name = self.name

        server_ip_address: Union[Unset, list[str]] = UNSET
        if not isinstance(self.server_ip_address, Unset):
            server_ip_address = self.server_ip_address

        status = self.status

        total_customers = self.total_customers

        total_sites = self.total_sites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if server_ip_address is not UNSET:
            field_dict["serverIpAddress"] = server_ip_address
        if status is not UNSET:
            field_dict["status"] = status
        if total_customers is not UNSET:
            field_dict["totalCustomers"] = total_customers
        if total_sites is not UNSET:
            field_dict["totalSites"] = total_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_producers_summary_response_200_info_item_created_at import (
            GetV1ExtranetsB2BProducersSummaryResponse200InfoItemCreatedAt,
        )

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1ExtranetsB2BProducersSummaryResponse200InfoItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1ExtranetsB2BProducersSummaryResponse200InfoItemCreatedAt.from_dict(_created_at)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        server_ip_address = cast(list[str], d.pop("serverIpAddress", UNSET))

        status = d.pop("status", UNSET)

        total_customers = d.pop("totalCustomers", UNSET)

        total_sites = d.pop("totalSites", UNSET)

        get_v1_extranets_b2b_producers_summary_response_200_info_item = cls(
            created_at=created_at,
            id=id,
            name=name,
            server_ip_address=server_ip_address,
            status=status,
            total_customers=total_customers,
            total_sites=total_sites,
        )

        get_v1_extranets_b2b_producers_summary_response_200_info_item.additional_properties = d
        return get_v1_extranets_b2b_producers_summary_response_200_info_item

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
