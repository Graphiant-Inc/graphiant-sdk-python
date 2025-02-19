from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_consumer_summary_response_200_summary_item_created_at import (
        GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItemCreatedAt,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItem")


@_attrs_define
class GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItem:
    """
    Attributes:
        b_2_b_status (Union[Unset, str]):  Example: TYPE_ENUM.
        created_at (Union[Unset, GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItemCreatedAt]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        num_edges (Union[Unset, str]):  Example: TYPE_UINT32.
        num_segments (Union[Unset, str]):  Example: TYPE_UINT32.
        num_sites (Union[Unset, str]):  Example: TYPE_UINT32.
        provider_name (Union[Unset, str]):  Example: TYPE_STRING.
        publisher_name (Union[Unset, str]):  Example: TYPE_STRING.
        service_name (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    b_2_b_status: Union[Unset, str] = UNSET
    created_at: Union[Unset, "GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItemCreatedAt"] = UNSET
    id: Union[Unset, str] = UNSET
    num_edges: Union[Unset, str] = UNSET
    num_segments: Union[Unset, str] = UNSET
    num_sites: Union[Unset, str] = UNSET
    provider_name: Union[Unset, str] = UNSET
    publisher_name: Union[Unset, str] = UNSET
    service_name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        b_2_b_status = self.b_2_b_status

        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        id = self.id

        num_edges = self.num_edges

        num_segments = self.num_segments

        num_sites = self.num_sites

        provider_name = self.provider_name

        publisher_name = self.publisher_name

        service_name = self.service_name

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if b_2_b_status is not UNSET:
            field_dict["b2bStatus"] = b_2_b_status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if num_edges is not UNSET:
            field_dict["numEdges"] = num_edges
        if num_segments is not UNSET:
            field_dict["numSegments"] = num_segments
        if num_sites is not UNSET:
            field_dict["numSites"] = num_sites
        if provider_name is not UNSET:
            field_dict["providerName"] = provider_name
        if publisher_name is not UNSET:
            field_dict["publisherName"] = publisher_name
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_consumer_summary_response_200_summary_item_created_at import (
            GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItemCreatedAt,
        )

        d = src_dict.copy()
        b_2_b_status = d.pop("b2bStatus", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1ExtranetsB2BConsumerSummaryResponse200SummaryItemCreatedAt.from_dict(_created_at)

        id = d.pop("id", UNSET)

        num_edges = d.pop("numEdges", UNSET)

        num_segments = d.pop("numSegments", UNSET)

        num_sites = d.pop("numSites", UNSET)

        provider_name = d.pop("providerName", UNSET)

        publisher_name = d.pop("publisherName", UNSET)

        service_name = d.pop("serviceName", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_extranets_b2b_consumer_summary_response_200_summary_item = cls(
            b_2_b_status=b_2_b_status,
            created_at=created_at,
            id=id,
            num_edges=num_edges,
            num_segments=num_segments,
            num_sites=num_sites,
            provider_name=provider_name,
            publisher_name=publisher_name,
            service_name=service_name,
            status=status,
            type_=type_,
        )

        get_v1_extranets_b2b_consumer_summary_response_200_summary_item.additional_properties = d
        return get_v1_extranets_b2b_consumer_summary_response_200_summary_item

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
