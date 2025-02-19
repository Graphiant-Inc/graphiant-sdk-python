from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MonitoringCircuitsSummaryResponse200SummariesItem")


@_attrs_define
class PostV1MonitoringCircuitsSummaryResponse200SummariesItem:
    """
    Attributes:
        admin_status (Union[Unset, str]):  Example: TYPE_BOOL.
        average_link_down_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        average_link_up_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        avg_mos (Union[Unset, str]):  Example: TYPE_FLOAT.
        config_link_down_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        config_link_up_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        connection_status (Union[Unset, str]):  Example: TYPE_ENUM.
        current_link_down_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        current_link_up_speed_kbps (Union[Unset, str]):  Example: TYPE_FLOAT.
        delay (Union[Unset, str]):  Example: TYPE_UINT64.
        jitter (Union[Unset, str]):  Example: TYPE_UINT64.
        loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        mos (Union[Unset, str]):  Example: TYPE_FLOAT.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    admin_status: Union[Unset, str] = UNSET
    average_link_down_speed_kbps: Union[Unset, str] = UNSET
    average_link_up_speed_kbps: Union[Unset, str] = UNSET
    avg_mos: Union[Unset, str] = UNSET
    config_link_down_speed_mbps: Union[Unset, str] = UNSET
    config_link_up_speed_mbps: Union[Unset, str] = UNSET
    connection_status: Union[Unset, str] = UNSET
    current_link_down_speed_kbps: Union[Unset, str] = UNSET
    current_link_up_speed_kbps: Union[Unset, str] = UNSET
    delay: Union[Unset, str] = UNSET
    jitter: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    mos: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_status = self.admin_status

        average_link_down_speed_kbps = self.average_link_down_speed_kbps

        average_link_up_speed_kbps = self.average_link_up_speed_kbps

        avg_mos = self.avg_mos

        config_link_down_speed_mbps = self.config_link_down_speed_mbps

        config_link_up_speed_mbps = self.config_link_up_speed_mbps

        connection_status = self.connection_status

        current_link_down_speed_kbps = self.current_link_down_speed_kbps

        current_link_up_speed_kbps = self.current_link_up_speed_kbps

        delay = self.delay

        jitter = self.jitter

        loss = self.loss

        mos = self.mos

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_status is not UNSET:
            field_dict["adminStatus"] = admin_status
        if average_link_down_speed_kbps is not UNSET:
            field_dict["averageLinkDownSpeedKbps"] = average_link_down_speed_kbps
        if average_link_up_speed_kbps is not UNSET:
            field_dict["averageLinkUpSpeedKbps"] = average_link_up_speed_kbps
        if avg_mos is not UNSET:
            field_dict["avgMos"] = avg_mos
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
        if loss is not UNSET:
            field_dict["loss"] = loss
        if mos is not UNSET:
            field_dict["mos"] = mos
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_status = d.pop("adminStatus", UNSET)

        average_link_down_speed_kbps = d.pop("averageLinkDownSpeedKbps", UNSET)

        average_link_up_speed_kbps = d.pop("averageLinkUpSpeedKbps", UNSET)

        avg_mos = d.pop("avgMos", UNSET)

        config_link_down_speed_mbps = d.pop("configLinkDownSpeedMbps", UNSET)

        config_link_up_speed_mbps = d.pop("configLinkUpSpeedMbps", UNSET)

        connection_status = d.pop("connectionStatus", UNSET)

        current_link_down_speed_kbps = d.pop("currentLinkDownSpeedKbps", UNSET)

        current_link_up_speed_kbps = d.pop("currentLinkUpSpeedKbps", UNSET)

        delay = d.pop("delay", UNSET)

        jitter = d.pop("jitter", UNSET)

        loss = d.pop("loss", UNSET)

        mos = d.pop("mos", UNSET)

        name = d.pop("name", UNSET)

        post_v1_monitoring_circuits_summary_response_200_summaries_item = cls(
            admin_status=admin_status,
            average_link_down_speed_kbps=average_link_down_speed_kbps,
            average_link_up_speed_kbps=average_link_up_speed_kbps,
            avg_mos=avg_mos,
            config_link_down_speed_mbps=config_link_down_speed_mbps,
            config_link_up_speed_mbps=config_link_up_speed_mbps,
            connection_status=connection_status,
            current_link_down_speed_kbps=current_link_down_speed_kbps,
            current_link_up_speed_kbps=current_link_up_speed_kbps,
            delay=delay,
            jitter=jitter,
            loss=loss,
            mos=mos,
            name=name,
        )

        post_v1_monitoring_circuits_summary_response_200_summaries_item.additional_properties = d
        return post_v1_monitoring_circuits_summary_response_200_summaries_item

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
