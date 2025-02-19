from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_dl_incidents import (
        PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemDlIncidents,
    )
    from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_total_incidents import (
        PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTotalIncidents,
    )
    from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_ts import (
        PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTs,
    )
    from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_ul_incidents import (
        PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemUlIncidents,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem")


@_attrs_define
class PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItem:
    """
    Attributes:
        dl_incidents (Union[Unset,
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemDlIncidents]):
        overall_status (Union[Unset, str]):  Example: TYPE_ENUM.
        total_incidents (Union[Unset,
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTotalIncidents]):
        ts (Union[Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTs]):
        ul_incidents (Union[Unset,
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemUlIncidents]):
    """

    dl_incidents: Union[
        Unset, "PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemDlIncidents"
    ] = UNSET
    overall_status: Union[Unset, str] = UNSET
    total_incidents: Union[
        Unset, "PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTotalIncidents"
    ] = UNSET
    ts: Union[Unset, "PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTs"] = UNSET
    ul_incidents: Union[
        Unset, "PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemUlIncidents"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dl_incidents: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dl_incidents, Unset):
            dl_incidents = self.dl_incidents.to_dict()

        overall_status = self.overall_status

        total_incidents: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.total_incidents, Unset):
            total_incidents = self.total_incidents.to_dict()

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        ul_incidents: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ul_incidents, Unset):
            ul_incidents = self.ul_incidents.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dl_incidents is not UNSET:
            field_dict["dlIncidents"] = dl_incidents
        if overall_status is not UNSET:
            field_dict["overallStatus"] = overall_status
        if total_incidents is not UNSET:
            field_dict["totalIncidents"] = total_incidents
        if ts is not UNSET:
            field_dict["ts"] = ts
        if ul_incidents is not UNSET:
            field_dict["ulIncidents"] = ul_incidents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_dl_incidents import (
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemDlIncidents,
        )
        from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_total_incidents import (
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTotalIncidents,
        )
        from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_ts import (
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTs,
        )
        from ..models.post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item_ul_incidents import (
            PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemUlIncidents,
        )

        d = src_dict.copy()
        _dl_incidents = d.pop("dlIncidents", UNSET)
        dl_incidents: Union[
            Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemDlIncidents
        ]
        if isinstance(_dl_incidents, Unset):
            dl_incidents = UNSET
        else:
            dl_incidents = (
                PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemDlIncidents.from_dict(
                    _dl_incidents
                )
            )

        overall_status = d.pop("overallStatus", UNSET)

        _total_incidents = d.pop("totalIncidents", UNSET)
        total_incidents: Union[
            Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTotalIncidents
        ]
        if isinstance(_total_incidents, Unset):
            total_incidents = UNSET
        else:
            total_incidents = (
                PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTotalIncidents.from_dict(
                    _total_incidents
                )
            )

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemTs.from_dict(_ts)

        _ul_incidents = d.pop("ulIncidents", UNSET)
        ul_incidents: Union[
            Unset, PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemUlIncidents
        ]
        if isinstance(_ul_incidents, Unset):
            ul_incidents = UNSET
        else:
            ul_incidents = (
                PostV2MonitoringCircuitsIncidentsResponse200CircuitIncidentsItemDataSamplesItemUlIncidents.from_dict(
                    _ul_incidents
                )
            )

        post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item = cls(
            dl_incidents=dl_incidents,
            overall_status=overall_status,
            total_incidents=total_incidents,
            ts=ts,
            ul_incidents=ul_incidents,
        )

        post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item.additional_properties = d
        return post_v2_monitoring_circuits_incidents_response_200_circuit_incidents_item_data_samples_item

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
