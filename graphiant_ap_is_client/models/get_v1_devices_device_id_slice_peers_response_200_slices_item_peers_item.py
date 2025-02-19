from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection,
    )
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem")


@_attrs_define
class GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem:
    """
    Attributes:
        bgp_connection (Union[Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection]):
        connection_quality (Union[Unset, str]):  Example: TYPE_ENUM.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        gdi (Union[Unset, str]):  Example: TYPE_UINT32.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        ipsec_connection (Union[Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection]):
        state (Union[Unset, str]):  Example: TYPE_STRING.
        wan_addresses (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    bgp_connection: Union[Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection"] = UNSET
    connection_quality: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    gdi: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    ipsec_connection: Union[Unset, "GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection"] = (
        UNSET
    )
    state: Union[Unset, str] = UNSET
    wan_addresses: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_connection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_connection, Unset):
            bgp_connection = self.bgp_connection.to_dict()

        connection_quality = self.connection_quality

        device_id = self.device_id

        gdi = self.gdi

        hostname = self.hostname

        ipsec_connection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipsec_connection, Unset):
            ipsec_connection = self.ipsec_connection.to_dict()

        state = self.state

        wan_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.wan_addresses, Unset):
            wan_addresses = self.wan_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_connection is not UNSET:
            field_dict["bgpConnection"] = bgp_connection
        if connection_quality is not UNSET:
            field_dict["connectionQuality"] = connection_quality
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if gdi is not UNSET:
            field_dict["gdi"] = gdi
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ipsec_connection is not UNSET:
            field_dict["ipsecConnection"] = ipsec_connection
        if state is not UNSET:
            field_dict["state"] = state
        if wan_addresses is not UNSET:
            field_dict["wanAddresses"] = wan_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_bgp_connection import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection,
        )
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item_ipsec_connection import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection,
        )

        d = src_dict.copy()
        _bgp_connection = d.pop("bgpConnection", UNSET)
        bgp_connection: Union[Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection]
        if isinstance(_bgp_connection, Unset):
            bgp_connection = UNSET
        else:
            bgp_connection = GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemBgpConnection.from_dict(
                _bgp_connection
            )

        connection_quality = d.pop("connectionQuality", UNSET)

        device_id = d.pop("deviceId", UNSET)

        gdi = d.pop("gdi", UNSET)

        hostname = d.pop("hostname", UNSET)

        _ipsec_connection = d.pop("ipsecConnection", UNSET)
        ipsec_connection: Union[Unset, GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection]
        if isinstance(_ipsec_connection, Unset):
            ipsec_connection = UNSET
        else:
            ipsec_connection = GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItemIpsecConnection.from_dict(
                _ipsec_connection
            )

        state = d.pop("state", UNSET)

        wan_addresses = cast(list[str], d.pop("wanAddresses", UNSET))

        get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item = cls(
            bgp_connection=bgp_connection,
            connection_quality=connection_quality,
            device_id=device_id,
            gdi=gdi,
            hostname=hostname,
            ipsec_connection=ipsec_connection,
            state=state,
            wan_addresses=wan_addresses,
        )

        get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item.additional_properties = d
        return get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item

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
