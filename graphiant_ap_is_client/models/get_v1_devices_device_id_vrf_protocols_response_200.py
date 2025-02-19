from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdVrfProtocolsResponse200")


@_attrs_define
class GetV1DevicesDeviceIdVrfProtocolsResponse200:
    """
    Attributes:
        bgp (Union[Unset, str]):  Example: TYPE_BOOL.
        connected (Union[Unset, str]):  Example: TYPE_BOOL.
        graphiant (Union[Unset, str]):  Example: TYPE_BOOL.
        ospfv2 (Union[Unset, str]):  Example: TYPE_BOOL.
        ospfv3 (Union[Unset, str]):  Example: TYPE_BOOL.
        static (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    bgp: Union[Unset, str] = UNSET
    connected: Union[Unset, str] = UNSET
    graphiant: Union[Unset, str] = UNSET
    ospfv2: Union[Unset, str] = UNSET
    ospfv3: Union[Unset, str] = UNSET
    static: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp = self.bgp

        connected = self.connected

        graphiant = self.graphiant

        ospfv2 = self.ospfv2

        ospfv3 = self.ospfv3

        static = self.static

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp is not UNSET:
            field_dict["bgp"] = bgp
        if connected is not UNSET:
            field_dict["connected"] = connected
        if graphiant is not UNSET:
            field_dict["graphiant"] = graphiant
        if ospfv2 is not UNSET:
            field_dict["ospfv2"] = ospfv2
        if ospfv3 is not UNSET:
            field_dict["ospfv3"] = ospfv3
        if static is not UNSET:
            field_dict["static"] = static

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bgp = d.pop("bgp", UNSET)

        connected = d.pop("connected", UNSET)

        graphiant = d.pop("graphiant", UNSET)

        ospfv2 = d.pop("ospfv2", UNSET)

        ospfv3 = d.pop("ospfv3", UNSET)

        static = d.pop("static", UNSET)

        get_v1_devices_device_id_vrf_protocols_response_200 = cls(
            bgp=bgp,
            connected=connected,
            graphiant=graphiant,
            ospfv2=ospfv2,
            ospfv3=ospfv3,
            static=static,
        )

        get_v1_devices_device_id_vrf_protocols_response_200.additional_properties = d
        return get_v1_devices_device_id_vrf_protocols_response_200

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
