from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceSnapshotResponse200SecondSnapshotData")


@_attrs_define
class GetV1DeviceSnapshotResponse200SecondSnapshotData:
    """
    Attributes:
        bfd_session_count (Union[Unset, str]):  Example: TYPE_INT32.
        bgp_neighbor_ip_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        bgp_session_count (Union[Unset, str]):  Example: TYPE_INT32.
        installed_labels (Union[Unset, str]):  Example: TYPE_INT32.
        ipsec_session_count (Union[Unset, str]):  Example: TYPE_INT32.
        ongoing_alerts (Union[Unset, str]):  Example: TYPE_INT32.
        ospf_neighbor_ip_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        ospf_session_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    bfd_session_count: Union[Unset, str] = UNSET
    bgp_neighbor_ip_list: Union[Unset, list[str]] = UNSET
    bgp_session_count: Union[Unset, str] = UNSET
    installed_labels: Union[Unset, str] = UNSET
    ipsec_session_count: Union[Unset, str] = UNSET
    ongoing_alerts: Union[Unset, str] = UNSET
    ospf_neighbor_ip_list: Union[Unset, list[str]] = UNSET
    ospf_session_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bfd_session_count = self.bfd_session_count

        bgp_neighbor_ip_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bgp_neighbor_ip_list, Unset):
            bgp_neighbor_ip_list = self.bgp_neighbor_ip_list

        bgp_session_count = self.bgp_session_count

        installed_labels = self.installed_labels

        ipsec_session_count = self.ipsec_session_count

        ongoing_alerts = self.ongoing_alerts

        ospf_neighbor_ip_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ospf_neighbor_ip_list, Unset):
            ospf_neighbor_ip_list = self.ospf_neighbor_ip_list

        ospf_session_count = self.ospf_session_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bfd_session_count is not UNSET:
            field_dict["bfdSessionCount"] = bfd_session_count
        if bgp_neighbor_ip_list is not UNSET:
            field_dict["bgpNeighborIpList"] = bgp_neighbor_ip_list
        if bgp_session_count is not UNSET:
            field_dict["bgpSessionCount"] = bgp_session_count
        if installed_labels is not UNSET:
            field_dict["installedLabels"] = installed_labels
        if ipsec_session_count is not UNSET:
            field_dict["ipsecSessionCount"] = ipsec_session_count
        if ongoing_alerts is not UNSET:
            field_dict["ongoingAlerts"] = ongoing_alerts
        if ospf_neighbor_ip_list is not UNSET:
            field_dict["ospfNeighborIpList"] = ospf_neighbor_ip_list
        if ospf_session_count is not UNSET:
            field_dict["ospfSessionCount"] = ospf_session_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bfd_session_count = d.pop("bfdSessionCount", UNSET)

        bgp_neighbor_ip_list = cast(list[str], d.pop("bgpNeighborIpList", UNSET))

        bgp_session_count = d.pop("bgpSessionCount", UNSET)

        installed_labels = d.pop("installedLabels", UNSET)

        ipsec_session_count = d.pop("ipsecSessionCount", UNSET)

        ongoing_alerts = d.pop("ongoingAlerts", UNSET)

        ospf_neighbor_ip_list = cast(list[str], d.pop("ospfNeighborIpList", UNSET))

        ospf_session_count = d.pop("ospfSessionCount", UNSET)

        get_v1_device_snapshot_response_200_second_snapshot_data = cls(
            bfd_session_count=bfd_session_count,
            bgp_neighbor_ip_list=bgp_neighbor_ip_list,
            bgp_session_count=bgp_session_count,
            installed_labels=installed_labels,
            ipsec_session_count=ipsec_session_count,
            ongoing_alerts=ongoing_alerts,
            ospf_neighbor_ip_list=ospf_neighbor_ip_list,
            ospf_session_count=ospf_session_count,
        )

        get_v1_device_snapshot_response_200_second_snapshot_data.additional_properties = d
        return get_v1_device_snapshot_response_200_second_snapshot_data

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
