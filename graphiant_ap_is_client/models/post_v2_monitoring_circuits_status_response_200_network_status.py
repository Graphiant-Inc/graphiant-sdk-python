from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_status_response_200_network_status_circuit_status import (
        PostV2MonitoringCircuitsStatusResponse200NetworkStatusCircuitStatus,
    )
    from ..models.post_v2_monitoring_circuits_status_response_200_network_status_core_status import (
        PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus,
    )
    from ..models.post_v2_monitoring_circuits_status_response_200_network_status_edges_status import (
        PostV2MonitoringCircuitsStatusResponse200NetworkStatusEdgesStatus,
    )
    from ..models.post_v2_monitoring_circuits_status_response_200_network_status_lan_status import (
        PostV2MonitoringCircuitsStatusResponse200NetworkStatusLanStatus,
    )
    from ..models.post_v2_monitoring_circuits_status_response_200_network_status_site_status import (
        PostV2MonitoringCircuitsStatusResponse200NetworkStatusSiteStatus,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsStatusResponse200NetworkStatus")


@_attrs_define
class PostV2MonitoringCircuitsStatusResponse200NetworkStatus:
    """
    Attributes:
        circuit_status (Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusCircuitStatus]):
        core_status (Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus]):
        edges_status (Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusEdgesStatus]):
        lan_status (Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusLanStatus]):
        site_status (Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusSiteStatus]):
    """

    circuit_status: Union[Unset, "PostV2MonitoringCircuitsStatusResponse200NetworkStatusCircuitStatus"] = UNSET
    core_status: Union[Unset, "PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus"] = UNSET
    edges_status: Union[Unset, "PostV2MonitoringCircuitsStatusResponse200NetworkStatusEdgesStatus"] = UNSET
    lan_status: Union[Unset, "PostV2MonitoringCircuitsStatusResponse200NetworkStatusLanStatus"] = UNSET
    site_status: Union[Unset, "PostV2MonitoringCircuitsStatusResponse200NetworkStatusSiteStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.circuit_status, Unset):
            circuit_status = self.circuit_status.to_dict()

        core_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.core_status, Unset):
            core_status = self.core_status.to_dict()

        edges_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges_status, Unset):
            edges_status = self.edges_status.to_dict()

        lan_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lan_status, Unset):
            lan_status = self.lan_status.to_dict()

        site_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site_status, Unset):
            site_status = self.site_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_status is not UNSET:
            field_dict["circuitStatus"] = circuit_status
        if core_status is not UNSET:
            field_dict["coreStatus"] = core_status
        if edges_status is not UNSET:
            field_dict["edgesStatus"] = edges_status
        if lan_status is not UNSET:
            field_dict["lanStatus"] = lan_status
        if site_status is not UNSET:
            field_dict["siteStatus"] = site_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_status_response_200_network_status_circuit_status import (
            PostV2MonitoringCircuitsStatusResponse200NetworkStatusCircuitStatus,
        )
        from ..models.post_v2_monitoring_circuits_status_response_200_network_status_core_status import (
            PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus,
        )
        from ..models.post_v2_monitoring_circuits_status_response_200_network_status_edges_status import (
            PostV2MonitoringCircuitsStatusResponse200NetworkStatusEdgesStatus,
        )
        from ..models.post_v2_monitoring_circuits_status_response_200_network_status_lan_status import (
            PostV2MonitoringCircuitsStatusResponse200NetworkStatusLanStatus,
        )
        from ..models.post_v2_monitoring_circuits_status_response_200_network_status_site_status import (
            PostV2MonitoringCircuitsStatusResponse200NetworkStatusSiteStatus,
        )

        d = src_dict.copy()
        _circuit_status = d.pop("circuitStatus", UNSET)
        circuit_status: Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusCircuitStatus]
        if isinstance(_circuit_status, Unset):
            circuit_status = UNSET
        else:
            circuit_status = PostV2MonitoringCircuitsStatusResponse200NetworkStatusCircuitStatus.from_dict(
                _circuit_status
            )

        _core_status = d.pop("coreStatus", UNSET)
        core_status: Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus]
        if isinstance(_core_status, Unset):
            core_status = UNSET
        else:
            core_status = PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus.from_dict(_core_status)

        _edges_status = d.pop("edgesStatus", UNSET)
        edges_status: Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusEdgesStatus]
        if isinstance(_edges_status, Unset):
            edges_status = UNSET
        else:
            edges_status = PostV2MonitoringCircuitsStatusResponse200NetworkStatusEdgesStatus.from_dict(_edges_status)

        _lan_status = d.pop("lanStatus", UNSET)
        lan_status: Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusLanStatus]
        if isinstance(_lan_status, Unset):
            lan_status = UNSET
        else:
            lan_status = PostV2MonitoringCircuitsStatusResponse200NetworkStatusLanStatus.from_dict(_lan_status)

        _site_status = d.pop("siteStatus", UNSET)
        site_status: Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatusSiteStatus]
        if isinstance(_site_status, Unset):
            site_status = UNSET
        else:
            site_status = PostV2MonitoringCircuitsStatusResponse200NetworkStatusSiteStatus.from_dict(_site_status)

        post_v2_monitoring_circuits_status_response_200_network_status = cls(
            circuit_status=circuit_status,
            core_status=core_status,
            edges_status=edges_status,
            lan_status=lan_status,
            site_status=site_status,
        )

        post_v2_monitoring_circuits_status_response_200_network_status.additional_properties = d
        return post_v2_monitoring_circuits_status_response_200_network_status

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
