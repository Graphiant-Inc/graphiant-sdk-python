from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1PortalPrivateInventoryDetailsResponse200DetailsItem")


@_attrs_define
class GetV1PortalPrivateInventoryDetailsResponse200DetailsItem:
    """
    Attributes:
        device_model (Union[Unset, str]):  Example: TYPE_STRING.
        device_serial (Union[Unset, str]):  Example: TYPE_STRING.
        private_gcs_id (Union[Unset, str]):  Example: TYPE_INT64.
        uuid (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_model: Union[Unset, str] = UNSET
    device_serial: Union[Unset, str] = UNSET
    private_gcs_id: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_model = self.device_model

        device_serial = self.device_serial

        private_gcs_id = self.private_gcs_id

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if device_serial is not UNSET:
            field_dict["deviceSerial"] = device_serial
        if private_gcs_id is not UNSET:
            field_dict["privateGcsId"] = private_gcs_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_model = d.pop("deviceModel", UNSET)

        device_serial = d.pop("deviceSerial", UNSET)

        private_gcs_id = d.pop("privateGcsId", UNSET)

        uuid = d.pop("uuid", UNSET)

        get_v1_portal_private_inventory_details_response_200_details_item = cls(
            device_model=device_model,
            device_serial=device_serial,
            private_gcs_id=private_gcs_id,
            uuid=uuid,
        )

        get_v1_portal_private_inventory_details_response_200_details_item.additional_properties = d
        return get_v1_portal_private_inventory_details_response_200_details_item

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
