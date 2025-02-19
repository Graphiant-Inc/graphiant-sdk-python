from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItemSnmpUsmRemoteUsersItem")


@_attrs_define
class GetV1DevicesResponse200DevicesItemSnmpUsmRemoteUsersItem:
    """
    Attributes:
        auth_loc_key (Union[Unset, str]):  Example: TYPE_STRING.
        auth_protocol (Union[Unset, str]):  Example: TYPE_ENUM.
        encryption_loc_key (Union[Unset, str]):  Example: TYPE_STRING.
        encryption_protocol (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    auth_loc_key: Union[Unset, str] = UNSET
    auth_protocol: Union[Unset, str] = UNSET
    encryption_loc_key: Union[Unset, str] = UNSET
    encryption_protocol: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_loc_key = self.auth_loc_key

        auth_protocol = self.auth_protocol

        encryption_loc_key = self.encryption_loc_key

        encryption_protocol = self.encryption_protocol

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_loc_key is not UNSET:
            field_dict["authLocKey"] = auth_loc_key
        if auth_protocol is not UNSET:
            field_dict["authProtocol"] = auth_protocol
        if encryption_loc_key is not UNSET:
            field_dict["encryptionLocKey"] = encryption_loc_key
        if encryption_protocol is not UNSET:
            field_dict["encryptionProtocol"] = encryption_protocol
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_loc_key = d.pop("authLocKey", UNSET)

        auth_protocol = d.pop("authProtocol", UNSET)

        encryption_loc_key = d.pop("encryptionLocKey", UNSET)

        encryption_protocol = d.pop("encryptionProtocol", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_v1_devices_response_200_devices_item_snmp_usm_remote_users_item = cls(
            auth_loc_key=auth_loc_key,
            auth_protocol=auth_protocol,
            encryption_loc_key=encryption_loc_key,
            encryption_protocol=encryption_protocol,
            id=id,
            name=name,
        )

        get_v1_devices_response_200_devices_item_snmp_usm_remote_users_item.additional_properties = d
        return get_v1_devices_response_200_devices_item_snmp_usm_remote_users_item

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
