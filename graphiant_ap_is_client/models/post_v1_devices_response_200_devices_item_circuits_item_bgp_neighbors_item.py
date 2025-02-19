from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_address_families_item import (
        PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemAddressFamiliesItem,
    )
    from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_bfd import (
        PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfd,
    )
    from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_bfd_neighbor import (
        PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfdNeighbor,
    )
    from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_time_since_last_oper_change import (
        PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemTimeSinceLastOperChange,
    )


T = TypeVar("T", bound="PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItem")


@_attrs_define
class PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItem:
    """
    Attributes:
        address_families (Union[Unset,
            list['PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemAddressFamiliesItem']]):
        bfd (Union[Unset, PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfd]):
        bfd_neighbor (Union[Unset, PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfdNeighbor]):
        bgp_type (Union[Unset, str]):  Example: TYPE_ENUM.
        default_originate (Union[Unset, str]):  Example: TYPE_ENUM.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        hold_timer (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        keepalive_timer (Union[Unset, str]):  Example: TYPE_UINT32.
        local_address (Union[Unset, str]):  Example: TYPE_STRING.
        local_interface (Union[Unset, str]):  Example: TYPE_STRING.
        max_prefix (Union[Unset, str]):  Example: 10000.
        md_5_password (Union[Unset, str]):  Example: TYPE_STRING.
        multi_hop (Union[Unset, str]):  Example: 5.
        peer_asn (Union[Unset, str]):  Example: TYPE_UINT32.
        remote_address (Union[Unset, str]):  Example: TYPE_STRING.
        send_community (Union[Unset, str]):  Example: default.
        state (Union[Unset, str]):  Example: TYPE_ENUM.
        time_since_last_oper_change (Union[Unset,
            PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemTimeSinceLastOperChange]):
        up (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    address_families: Union[
        Unset, list["PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemAddressFamiliesItem"]
    ] = UNSET
    bfd: Union[Unset, "PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfd"] = UNSET
    bfd_neighbor: Union[Unset, "PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfdNeighbor"] = UNSET
    bgp_type: Union[Unset, str] = UNSET
    default_originate: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    hold_timer: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    keepalive_timer: Union[Unset, str] = UNSET
    local_address: Union[Unset, str] = UNSET
    local_interface: Union[Unset, str] = UNSET
    max_prefix: Union[Unset, str] = UNSET
    md_5_password: Union[Unset, str] = UNSET
    multi_hop: Union[Unset, str] = UNSET
    peer_asn: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    send_community: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    time_since_last_oper_change: Union[
        Unset, "PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemTimeSinceLastOperChange"
    ] = UNSET
    up: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_families: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.address_families, Unset):
            address_families = []
            for address_families_item_data in self.address_families:
                address_families_item = address_families_item_data.to_dict()
                address_families.append(address_families_item)

        bfd: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bfd, Unset):
            bfd = self.bfd.to_dict()

        bfd_neighbor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bfd_neighbor, Unset):
            bfd_neighbor = self.bfd_neighbor.to_dict()

        bgp_type = self.bgp_type

        default_originate = self.default_originate

        enabled = self.enabled

        hold_timer = self.hold_timer

        id = self.id

        keepalive_timer = self.keepalive_timer

        local_address = self.local_address

        local_interface = self.local_interface

        max_prefix = self.max_prefix

        md_5_password = self.md_5_password

        multi_hop = self.multi_hop

        peer_asn = self.peer_asn

        remote_address = self.remote_address

        send_community = self.send_community

        state = self.state

        time_since_last_oper_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_since_last_oper_change, Unset):
            time_since_last_oper_change = self.time_since_last_oper_change.to_dict()

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_families is not UNSET:
            field_dict["addressFamilies"] = address_families
        if bfd is not UNSET:
            field_dict["bfd"] = bfd
        if bfd_neighbor is not UNSET:
            field_dict["bfdNeighbor"] = bfd_neighbor
        if bgp_type is not UNSET:
            field_dict["bgpType"] = bgp_type
        if default_originate is not UNSET:
            field_dict["defaultOriginate"] = default_originate
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if hold_timer is not UNSET:
            field_dict["holdTimer"] = hold_timer
        if id is not UNSET:
            field_dict["id"] = id
        if keepalive_timer is not UNSET:
            field_dict["keepaliveTimer"] = keepalive_timer
        if local_address is not UNSET:
            field_dict["localAddress"] = local_address
        if local_interface is not UNSET:
            field_dict["localInterface"] = local_interface
        if max_prefix is not UNSET:
            field_dict["maxPrefix"] = max_prefix
        if md_5_password is not UNSET:
            field_dict["md5Password"] = md_5_password
        if multi_hop is not UNSET:
            field_dict["multiHop"] = multi_hop
        if peer_asn is not UNSET:
            field_dict["peerAsn"] = peer_asn
        if remote_address is not UNSET:
            field_dict["remoteAddress"] = remote_address
        if send_community is not UNSET:
            field_dict["sendCommunity"] = send_community
        if state is not UNSET:
            field_dict["state"] = state
        if time_since_last_oper_change is not UNSET:
            field_dict["timeSinceLastOperChange"] = time_since_last_oper_change
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_address_families_item import (
            PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemAddressFamiliesItem,
        )
        from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_bfd import (
            PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfd,
        )
        from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_bfd_neighbor import (
            PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfdNeighbor,
        )
        from ..models.post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item_time_since_last_oper_change import (
            PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemTimeSinceLastOperChange,
        )

        d = src_dict.copy()
        address_families = []
        _address_families = d.pop("addressFamilies", UNSET)
        for address_families_item_data in _address_families or []:
            address_families_item = (
                PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemAddressFamiliesItem.from_dict(
                    address_families_item_data
                )
            )

            address_families.append(address_families_item)

        _bfd = d.pop("bfd", UNSET)
        bfd: Union[Unset, PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfd]
        if isinstance(_bfd, Unset):
            bfd = UNSET
        else:
            bfd = PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfd.from_dict(_bfd)

        _bfd_neighbor = d.pop("bfdNeighbor", UNSET)
        bfd_neighbor: Union[Unset, PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfdNeighbor]
        if isinstance(_bfd_neighbor, Unset):
            bfd_neighbor = UNSET
        else:
            bfd_neighbor = PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemBfdNeighbor.from_dict(
                _bfd_neighbor
            )

        bgp_type = d.pop("bgpType", UNSET)

        default_originate = d.pop("defaultOriginate", UNSET)

        enabled = d.pop("enabled", UNSET)

        hold_timer = d.pop("holdTimer", UNSET)

        id = d.pop("id", UNSET)

        keepalive_timer = d.pop("keepaliveTimer", UNSET)

        local_address = d.pop("localAddress", UNSET)

        local_interface = d.pop("localInterface", UNSET)

        max_prefix = d.pop("maxPrefix", UNSET)

        md_5_password = d.pop("md5Password", UNSET)

        multi_hop = d.pop("multiHop", UNSET)

        peer_asn = d.pop("peerAsn", UNSET)

        remote_address = d.pop("remoteAddress", UNSET)

        send_community = d.pop("sendCommunity", UNSET)

        state = d.pop("state", UNSET)

        _time_since_last_oper_change = d.pop("timeSinceLastOperChange", UNSET)
        time_since_last_oper_change: Union[
            Unset, PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemTimeSinceLastOperChange
        ]
        if isinstance(_time_since_last_oper_change, Unset):
            time_since_last_oper_change = UNSET
        else:
            time_since_last_oper_change = (
                PostV1DevicesResponse200DevicesItemCircuitsItemBgpNeighborsItemTimeSinceLastOperChange.from_dict(
                    _time_since_last_oper_change
                )
            )

        up = d.pop("up", UNSET)

        post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item = cls(
            address_families=address_families,
            bfd=bfd,
            bfd_neighbor=bfd_neighbor,
            bgp_type=bgp_type,
            default_originate=default_originate,
            enabled=enabled,
            hold_timer=hold_timer,
            id=id,
            keepalive_timer=keepalive_timer,
            local_address=local_address,
            local_interface=local_interface,
            max_prefix=max_prefix,
            md_5_password=md_5_password,
            multi_hop=multi_hop,
            peer_asn=peer_asn,
            remote_address=remote_address,
            send_community=send_community,
            state=state,
            time_since_last_oper_change=time_since_last_oper_change,
            up=up,
        )

        post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item.additional_properties = d
        return post_v1_devices_response_200_devices_item_circuits_item_bgp_neighbors_item

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
