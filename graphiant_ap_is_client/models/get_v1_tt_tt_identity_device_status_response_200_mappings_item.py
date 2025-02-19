from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_tt_tt_identity_device_status_response_200_mappings_item_connect_time import (
        GetV1TtTtIdentityDeviceStatusResponse200MappingsItemConnectTime,
    )


T = TypeVar("T", bound="GetV1TtTtIdentityDeviceStatusResponse200MappingsItem")


@_attrs_define
class GetV1TtTtIdentityDeviceStatusResponse200MappingsItem:
    """
    Attributes:
        connect_time (Union[Unset, GetV1TtTtIdentityDeviceStatusResponse200MappingsItemConnectTime]):
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        enterprise_id (Union[Unset, str]):  Example: TYPE_UINT64.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        ipaddress (Union[Unset, str]):  Example: TYPE_STRING.
        tt_identity (Union[Unset, str]):  Example: TYPE_STRING.
    """

    connect_time: Union[Unset, "GetV1TtTtIdentityDeviceStatusResponse200MappingsItemConnectTime"] = UNSET
    device_id: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    ipaddress: Union[Unset, str] = UNSET
    tt_identity: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connect_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connect_time, Unset):
            connect_time = self.connect_time.to_dict()

        device_id = self.device_id

        enterprise_id = self.enterprise_id

        hostname = self.hostname

        ipaddress = self.ipaddress

        tt_identity = self.tt_identity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connect_time is not UNSET:
            field_dict["connectTime"] = connect_time
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ipaddress is not UNSET:
            field_dict["ipaddress"] = ipaddress
        if tt_identity is not UNSET:
            field_dict["ttIdentity"] = tt_identity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_tt_tt_identity_device_status_response_200_mappings_item_connect_time import (
            GetV1TtTtIdentityDeviceStatusResponse200MappingsItemConnectTime,
        )

        d = src_dict.copy()
        _connect_time = d.pop("connectTime", UNSET)
        connect_time: Union[Unset, GetV1TtTtIdentityDeviceStatusResponse200MappingsItemConnectTime]
        if isinstance(_connect_time, Unset):
            connect_time = UNSET
        else:
            connect_time = GetV1TtTtIdentityDeviceStatusResponse200MappingsItemConnectTime.from_dict(_connect_time)

        device_id = d.pop("deviceId", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        hostname = d.pop("hostname", UNSET)

        ipaddress = d.pop("ipaddress", UNSET)

        tt_identity = d.pop("ttIdentity", UNSET)

        get_v1_tt_tt_identity_device_status_response_200_mappings_item = cls(
            connect_time=connect_time,
            device_id=device_id,
            enterprise_id=enterprise_id,
            hostname=hostname,
            ipaddress=ipaddress,
            tt_identity=tt_identity,
        )

        get_v1_tt_tt_identity_device_status_response_200_mappings_item.additional_properties = d
        return get_v1_tt_tt_identity_device_status_response_200_mappings_item

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
