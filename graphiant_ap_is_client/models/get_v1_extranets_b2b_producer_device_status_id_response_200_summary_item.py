from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item_created_at import (
        GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItemCreatedAt,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem")


@_attrs_define
class GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem:
    """
    Attributes:
        created_at (Union[Unset, GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItemCreatedAt]):
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        location (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    created_at: Union[Unset, "GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItemCreatedAt"] = UNSET
    device_id: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        device_id = self.device_id

        location = self.location

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item_created_at import (
            GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItemCreatedAt,
        )

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItemCreatedAt.from_dict(_created_at)

        device_id = d.pop("deviceId", UNSET)

        location = d.pop("location", UNSET)

        status = d.pop("status", UNSET)

        get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item = cls(
            created_at=created_at,
            device_id=device_id,
            location=location,
            status=status,
        )

        get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item.additional_properties = d
        return get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item

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
