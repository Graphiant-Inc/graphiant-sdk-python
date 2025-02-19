from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem")


@_attrs_define
class PostV2MonitoringCircuitsSummaryResponse200CircuitSummariesItem:
    """
    Attributes:
        average_delay (Union[Unset, str]):  Example: TYPE_FLOAT.
        average_jitter (Union[Unset, str]):  Example: TYPE_FLOAT.
        average_link_down_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        average_link_up_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        average_loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        avg_mos (Union[Unset, str]):  Example: TYPE_FLOAT.
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        config_link_down_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        config_link_up_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        connection_status (Union[Unset, str]):  Example: TYPE_ENUM.
        current_link_down_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        current_link_up_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        delay (Union[Unset, str]):  Example: TYPE_UINT64.
        jitter (Union[Unset, str]):  Example: TYPE_UINT64.
        last_resort (Union[Unset, str]):  Example: TYPE_BOOL.
        loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        max_delay (Union[Unset, str]):  Example: TYPE_FLOAT.
        max_jitter (Union[Unset, str]):  Example: TYPE_FLOAT.
        max_loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        max_mos (Union[Unset, str]):  Example: TYPE_FLOAT.
        min_delay (Union[Unset, str]):  Example: TYPE_FLOAT.
        min_jitter (Union[Unset, str]):  Example: TYPE_FLOAT.
        min_loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        min_mos (Union[Unset, str]):  Example: TYPE_FLOAT.
        mos (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    average_delay: Union[Unset, str] = UNSET
    average_jitter: Union[Unset, str] = UNSET
    average_link_down_speed_kbps: Union[Unset, str] = UNSET
    average_link_up_speed_kbps: Union[Unset, str] = UNSET
    average_loss: Union[Unset, str] = UNSET
    avg_mos: Union[Unset, str] = UNSET
    circuit_name: Union[Unset, str] = UNSET
    config_link_down_speed_mbps: Union[Unset, str] = UNSET
    config_link_up_speed_mbps: Union[Unset, str] = UNSET
    connection_status: Union[Unset, str] = UNSET
    current_link_down_speed_kbps: Union[Unset, str] = UNSET
    current_link_up_speed_kbps: Union[Unset, str] = UNSET
    delay: Union[Unset, str] = UNSET
    jitter: Union[Unset, str] = UNSET
    last_resort: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    max_delay: Union[Unset, str] = UNSET
    max_jitter: Union[Unset, str] = UNSET
    max_loss: Union[Unset, str] = UNSET
    max_mos: Union[Unset, str] = UNSET
    min_delay: Union[Unset, str] = UNSET
    min_jitter: Union[Unset, str] = UNSET
    min_loss: Union[Unset, str] = UNSET
    min_mos: Union[Unset, str] = UNSET
    mos: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_delay = self.average_delay

        average_jitter = self.average_jitter

        average_link_down_speed_kbps = self.average_link_down_speed_kbps

        average_link_up_speed_kbps = self.average_link_up_speed_kbps

        average_loss = self.average_loss

        avg_mos = self.avg_mos

        circuit_name = self.circuit_name

        config_link_down_speed_mbps = self.config_link_down_speed_mbps

        config_link_up_speed_mbps = self.config_link_up_speed_mbps

        connection_status = self.connection_status

        current_link_down_speed_kbps = self.current_link_down_speed_kbps

        current_link_up_speed_kbps = self.current_link_up_speed_kbps

        delay = self.delay

        jitter = self.jitter

        last_resort = self.last_resort

        loss = self.loss

        max_delay = self.max_delay

        max_jitter = self.max_jitter

        max_loss = self.max_loss

        max_mos = self.max_mos

        min_delay = self.min_delay

        min_jitter = self.min_jitter

        min_loss = self.min_loss

        min_mos = self.min_mos

        mos = self.mos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_delay is not UNSET:
            field_dict["averageDelay"] = average_delay
        if average_jitter is not UNSET:
            field_dict["averageJitter"] = average_jitter
        if average_link_down_speed_kbps is not UNSET:
            field_dict["averageLinkDownSpeedKbps"] = average_link_down_speed_kbps
        if average_link_up_speed_kbps is not UNSET:
            field_dict["averageLinkUpSpeedKbps"] = average_link_up_speed_kbps
        if average_loss is not UNSET:
            field_dict["averageLoss"] = average_loss
        if avg_mos is not UNSET:
            field_dict["avgMos"] = avg_mos
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if config_link_down_speed_mbps is not UNSET:
            field_dict["configLinkDownSpeedMbps"] = config_link_down_speed_mbps
        if config_link_up_speed_mbps is not UNSET:
            field_dict["configLinkUpSpeedMbps"] = config_link_up_speed_mbps
        if connection_status is not UNSET:
            field_dict["connectionStatus"] = connection_status
        if current_link_down_speed_kbps is not UNSET:
            field_dict["currentLinkDownSpeedKbps"] = current_link_down_speed_kbps
        if current_link_up_speed_kbps is not UNSET:
            field_dict["currentLinkUpSpeedKbps"] = current_link_up_speed_kbps
        if delay is not UNSET:
            field_dict["delay"] = delay
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if last_resort is not UNSET:
            field_dict["lastResort"] = last_resort
        if loss is not UNSET:
            field_dict["loss"] = loss
        if max_delay is not UNSET:
            field_dict["maxDelay"] = max_delay
        if max_jitter is not UNSET:
            field_dict["maxJitter"] = max_jitter
        if max_loss is not UNSET:
            field_dict["maxLoss"] = max_loss
        if max_mos is not UNSET:
            field_dict["maxMos"] = max_mos
        if min_delay is not UNSET:
            field_dict["minDelay"] = min_delay
        if min_jitter is not UNSET:
            field_dict["minJitter"] = min_jitter
        if min_loss is not UNSET:
            field_dict["minLoss"] = min_loss
        if min_mos is not UNSET:
            field_dict["minMos"] = min_mos
        if mos is not UNSET:
            field_dict["mos"] = mos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        average_delay = d.pop("averageDelay", UNSET)

        average_jitter = d.pop("averageJitter", UNSET)

        average_link_down_speed_kbps = d.pop("averageLinkDownSpeedKbps", UNSET)

        average_link_up_speed_kbps = d.pop("averageLinkUpSpeedKbps", UNSET)

        average_loss = d.pop("averageLoss", UNSET)

        avg_mos = d.pop("avgMos", UNSET)

        circuit_name = d.pop("circuitName", UNSET)

        config_link_down_speed_mbps = d.pop("configLinkDownSpeedMbps", UNSET)

        config_link_up_speed_mbps = d.pop("configLinkUpSpeedMbps", UNSET)

        connection_status = d.pop("connectionStatus", UNSET)

        current_link_down_speed_kbps = d.pop("currentLinkDownSpeedKbps", UNSET)

        current_link_up_speed_kbps = d.pop("currentLinkUpSpeedKbps", UNSET)

        delay = d.pop("delay", UNSET)

        jitter = d.pop("jitter", UNSET)

        last_resort = d.pop("lastResort", UNSET)

        loss = d.pop("loss", UNSET)

        max_delay = d.pop("maxDelay", UNSET)

        max_jitter = d.pop("maxJitter", UNSET)

        max_loss = d.pop("maxLoss", UNSET)

        max_mos = d.pop("maxMos", UNSET)

        min_delay = d.pop("minDelay", UNSET)

        min_jitter = d.pop("minJitter", UNSET)

        min_loss = d.pop("minLoss", UNSET)

        min_mos = d.pop("minMos", UNSET)

        mos = d.pop("mos", UNSET)

        post_v2_monitoring_circuits_summary_response_200_circuit_summaries_item = cls(
            average_delay=average_delay,
            average_jitter=average_jitter,
            average_link_down_speed_kbps=average_link_down_speed_kbps,
            average_link_up_speed_kbps=average_link_up_speed_kbps,
            average_loss=average_loss,
            avg_mos=avg_mos,
            circuit_name=circuit_name,
            config_link_down_speed_mbps=config_link_down_speed_mbps,
            config_link_up_speed_mbps=config_link_up_speed_mbps,
            connection_status=connection_status,
            current_link_down_speed_kbps=current_link_down_speed_kbps,
            current_link_up_speed_kbps=current_link_up_speed_kbps,
            delay=delay,
            jitter=jitter,
            last_resort=last_resort,
            loss=loss,
            max_delay=max_delay,
            max_jitter=max_jitter,
            max_loss=max_loss,
            max_mos=max_mos,
            min_delay=min_delay,
            min_jitter=min_jitter,
            min_loss=min_loss,
            min_mos=min_mos,
            mos=mos,
        )

        post_v2_monitoring_circuits_summary_response_200_circuit_summaries_item.additional_properties = d
        return post_v2_monitoring_circuits_summary_response_200_circuit_summaries_item

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
