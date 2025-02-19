from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_bringup_response_200_summaries_item_first_appeared_on import (
        PostV1DevicesBringupResponse200SummariesItemFirstAppearedOn,
    )


T = TypeVar("T", bound="PostV1DevicesBringupResponse200SummariesItem")


@_attrs_define
class PostV1DevicesBringupResponse200SummariesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        discovered_location (Union[Unset, str]):  Example: TYPE_STRING.
        first_appeared_on (Union[Unset, PostV1DevicesBringupResponse200SummariesItemFirstAppearedOn]):
        ip_detected (Union[Unset, str]):  Example: TYPE_STRING.
        is_new (Union[Unset, str]):  Example: TYPE_BOOL.
        state (Union[Unset, str]):  Example: TYPE_ENUM.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    discovered_location: Union[Unset, str] = UNSET
    first_appeared_on: Union[Unset, "PostV1DevicesBringupResponse200SummariesItemFirstAppearedOn"] = UNSET
    ip_detected: Union[Unset, str] = UNSET
    is_new: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        discovered_location = self.discovered_location

        first_appeared_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_appeared_on, Unset):
            first_appeared_on = self.first_appeared_on.to_dict()

        ip_detected = self.ip_detected

        is_new = self.is_new

        state = self.state

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if discovered_location is not UNSET:
            field_dict["discoveredLocation"] = discovered_location
        if first_appeared_on is not UNSET:
            field_dict["firstAppearedOn"] = first_appeared_on
        if ip_detected is not UNSET:
            field_dict["ipDetected"] = ip_detected
        if is_new is not UNSET:
            field_dict["isNew"] = is_new
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_bringup_response_200_summaries_item_first_appeared_on import (
            PostV1DevicesBringupResponse200SummariesItemFirstAppearedOn,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        discovered_location = d.pop("discoveredLocation", UNSET)

        _first_appeared_on = d.pop("firstAppearedOn", UNSET)
        first_appeared_on: Union[Unset, PostV1DevicesBringupResponse200SummariesItemFirstAppearedOn]
        if isinstance(_first_appeared_on, Unset):
            first_appeared_on = UNSET
        else:
            first_appeared_on = PostV1DevicesBringupResponse200SummariesItemFirstAppearedOn.from_dict(
                _first_appeared_on
            )

        ip_detected = d.pop("ipDetected", UNSET)

        is_new = d.pop("isNew", UNSET)

        state = d.pop("state", UNSET)

        status = d.pop("status", UNSET)

        post_v1_devices_bringup_response_200_summaries_item = cls(
            device_id=device_id,
            discovered_location=discovered_location,
            first_appeared_on=first_appeared_on,
            ip_detected=ip_detected,
            is_new=is_new,
            state=state,
            status=status,
        )

        post_v1_devices_bringup_response_200_summaries_item.additional_properties = d
        return post_v1_devices_bringup_response_200_summaries_item

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
