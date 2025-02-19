from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_filter_response_200_circuits_item import (
        GetV1BackboneHealthFilterResponse200CircuitsItem,
    )
    from ..models.get_v1_backbone_health_filter_response_200_devices_item import (
        GetV1BackboneHealthFilterResponse200DevicesItem,
    )
    from ..models.get_v1_backbone_health_filter_response_200_lan_segments_item import (
        GetV1BackboneHealthFilterResponse200LanSegmentsItem,
    )
    from ..models.get_v1_backbone_health_filter_response_200_regions_item import (
        GetV1BackboneHealthFilterResponse200RegionsItem,
    )
    from ..models.get_v1_backbone_health_filter_response_200_sites_item import (
        GetV1BackboneHealthFilterResponse200SitesItem,
    )


T = TypeVar("T", bound="GetV1BackboneHealthFilterResponse200")


@_attrs_define
class GetV1BackboneHealthFilterResponse200:
    """
    Attributes:
        circuits (Union[Unset, list['GetV1BackboneHealthFilterResponse200CircuitsItem']]):
        devices (Union[Unset, list['GetV1BackboneHealthFilterResponse200DevicesItem']]):
        lan_segments (Union[Unset, list['GetV1BackboneHealthFilterResponse200LanSegmentsItem']]):
        regions (Union[Unset, list['GetV1BackboneHealthFilterResponse200RegionsItem']]):
        sites (Union[Unset, list['GetV1BackboneHealthFilterResponse200SitesItem']]):
    """

    circuits: Union[Unset, list["GetV1BackboneHealthFilterResponse200CircuitsItem"]] = UNSET
    devices: Union[Unset, list["GetV1BackboneHealthFilterResponse200DevicesItem"]] = UNSET
    lan_segments: Union[Unset, list["GetV1BackboneHealthFilterResponse200LanSegmentsItem"]] = UNSET
    regions: Union[Unset, list["GetV1BackboneHealthFilterResponse200RegionsItem"]] = UNSET
    sites: Union[Unset, list["GetV1BackboneHealthFilterResponse200SitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = []
            for circuits_item_data in self.circuits:
                circuits_item = circuits_item_data.to_dict()
                circuits.append(circuits_item)

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        lan_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lan_segments, Unset):
            lan_segments = []
            for lan_segments_item_data in self.lan_segments:
                lan_segments_item = lan_segments_item_data.to_dict()
                lan_segments.append(lan_segments_item)

        regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuits is not UNSET:
            field_dict["circuits"] = circuits
        if devices is not UNSET:
            field_dict["devices"] = devices
        if lan_segments is not UNSET:
            field_dict["lanSegments"] = lan_segments
        if regions is not UNSET:
            field_dict["regions"] = regions
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_filter_response_200_circuits_item import (
            GetV1BackboneHealthFilterResponse200CircuitsItem,
        )
        from ..models.get_v1_backbone_health_filter_response_200_devices_item import (
            GetV1BackboneHealthFilterResponse200DevicesItem,
        )
        from ..models.get_v1_backbone_health_filter_response_200_lan_segments_item import (
            GetV1BackboneHealthFilterResponse200LanSegmentsItem,
        )
        from ..models.get_v1_backbone_health_filter_response_200_regions_item import (
            GetV1BackboneHealthFilterResponse200RegionsItem,
        )
        from ..models.get_v1_backbone_health_filter_response_200_sites_item import (
            GetV1BackboneHealthFilterResponse200SitesItem,
        )

        d = src_dict.copy()
        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = GetV1BackboneHealthFilterResponse200CircuitsItem.from_dict(circuits_item_data)

            circuits.append(circuits_item)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetV1BackboneHealthFilterResponse200DevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        lan_segments = []
        _lan_segments = d.pop("lanSegments", UNSET)
        for lan_segments_item_data in _lan_segments or []:
            lan_segments_item = GetV1BackboneHealthFilterResponse200LanSegmentsItem.from_dict(lan_segments_item_data)

            lan_segments.append(lan_segments_item)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = GetV1BackboneHealthFilterResponse200RegionsItem.from_dict(regions_item_data)

            regions.append(regions_item)

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = GetV1BackboneHealthFilterResponse200SitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        get_v1_backbone_health_filter_response_200 = cls(
            circuits=circuits,
            devices=devices,
            lan_segments=lan_segments,
            regions=regions,
            sites=sites,
        )

        get_v1_backbone_health_filter_response_200.additional_properties = d
        return get_v1_backbone_health_filter_response_200

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
