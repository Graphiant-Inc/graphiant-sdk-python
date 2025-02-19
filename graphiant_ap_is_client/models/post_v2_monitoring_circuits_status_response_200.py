from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_status_response_200_circuits_item import (
        PostV2MonitoringCircuitsStatusResponse200CircuitsItem,
    )
    from ..models.post_v2_monitoring_circuits_status_response_200_network_status import (
        PostV2MonitoringCircuitsStatusResponse200NetworkStatus,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsStatusResponse200")


@_attrs_define
class PostV2MonitoringCircuitsStatusResponse200:
    """
    Attributes:
        circuits (Union[Unset, list['PostV2MonitoringCircuitsStatusResponse200CircuitsItem']]):
        network_status (Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatus]):
    """

    circuits: Union[Unset, list["PostV2MonitoringCircuitsStatusResponse200CircuitsItem"]] = UNSET
    network_status: Union[Unset, "PostV2MonitoringCircuitsStatusResponse200NetworkStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = []
            for circuits_item_data in self.circuits:
                circuits_item = circuits_item_data.to_dict()
                circuits.append(circuits_item)

        network_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network_status, Unset):
            network_status = self.network_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuits is not UNSET:
            field_dict["circuits"] = circuits
        if network_status is not UNSET:
            field_dict["networkStatus"] = network_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_status_response_200_circuits_item import (
            PostV2MonitoringCircuitsStatusResponse200CircuitsItem,
        )
        from ..models.post_v2_monitoring_circuits_status_response_200_network_status import (
            PostV2MonitoringCircuitsStatusResponse200NetworkStatus,
        )

        d = src_dict.copy()
        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = PostV2MonitoringCircuitsStatusResponse200CircuitsItem.from_dict(circuits_item_data)

            circuits.append(circuits_item)

        _network_status = d.pop("networkStatus", UNSET)
        network_status: Union[Unset, PostV2MonitoringCircuitsStatusResponse200NetworkStatus]
        if isinstance(_network_status, Unset):
            network_status = UNSET
        else:
            network_status = PostV2MonitoringCircuitsStatusResponse200NetworkStatus.from_dict(_network_status)

        post_v2_monitoring_circuits_status_response_200 = cls(
            circuits=circuits,
            network_status=network_status,
        )

        post_v2_monitoring_circuits_status_response_200.additional_properties = d
        return post_v2_monitoring_circuits_status_response_200

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
