from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item import (
        PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem,
    )
    from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_selector import (
        PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSelector,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemData")


@_attrs_define
class PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemData:
    """
    Attributes:
        samples (Union[Unset, list['PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem']]):
        selector (Union[Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSelector]):
    """

    samples: Union[Unset, list["PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem"]] = (
        UNSET
    )
    selector: Union[Unset, "PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSelector"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        samples: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.samples, Unset):
            samples = []
            for samples_item_data in self.samples:
                samples_item = samples_item_data.to_dict()
                samples.append(samples_item)

        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if samples is not UNSET:
            field_dict["samples"] = samples
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item import (
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem,
        )
        from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_selector import (
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSelector,
        )

        d = src_dict.copy()
        samples = []
        _samples = d.pop("samples", UNSET)
        for samples_item_data in _samples or []:
            samples_item = PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem.from_dict(
                samples_item_data
            )

            samples.append(samples_item)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSelector.from_dict(_selector)

        post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data = cls(
            samples=samples,
            selector=selector,
        )

        post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data.additional_properties = d
        return post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data

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
