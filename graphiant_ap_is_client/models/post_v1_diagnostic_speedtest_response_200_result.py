from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_speedtest_response_200_result_date_time import (
        PostV1DiagnosticSpeedtestResponse200ResultDateTime,
    )
    from ..models.post_v1_diagnostic_speedtest_response_200_result_server_details import (
        PostV1DiagnosticSpeedtestResponse200ResultServerDetails,
    )


T = TypeVar("T", bound="PostV1DiagnosticSpeedtestResponse200Result")


@_attrs_define
class PostV1DiagnosticSpeedtestResponse200Result:
    """
    Attributes:
        avg_ping_time (Union[Unset, str]):  Example: 3.
        date_time (Union[Unset, PostV1DiagnosticSpeedtestResponse200ResultDateTime]):
        download_speed (Union[Unset, str]):  Example: 30.1.
        isp (Union[Unset, str]):  Example: Google Fiber.
        max_ping_time (Union[Unset, str]):  Example: 5.
        min_ping_time (Union[Unset, str]):  Example: 10.
        result (Union[Unset, str]):  Example: Failed.
        server_details (Union[Unset, PostV1DiagnosticSpeedtestResponse200ResultServerDetails]):
        upload_speed (Union[Unset, str]):  Example: 21.
    """

    avg_ping_time: Union[Unset, str] = UNSET
    date_time: Union[Unset, "PostV1DiagnosticSpeedtestResponse200ResultDateTime"] = UNSET
    download_speed: Union[Unset, str] = UNSET
    isp: Union[Unset, str] = UNSET
    max_ping_time: Union[Unset, str] = UNSET
    min_ping_time: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    server_details: Union[Unset, "PostV1DiagnosticSpeedtestResponse200ResultServerDetails"] = UNSET
    upload_speed: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_ping_time = self.avg_ping_time

        date_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.to_dict()

        download_speed = self.download_speed

        isp = self.isp

        max_ping_time = self.max_ping_time

        min_ping_time = self.min_ping_time

        result = self.result

        server_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_details, Unset):
            server_details = self.server_details.to_dict()

        upload_speed = self.upload_speed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_ping_time is not UNSET:
            field_dict["avgPingTime"] = avg_ping_time
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if download_speed is not UNSET:
            field_dict["downloadSpeed"] = download_speed
        if isp is not UNSET:
            field_dict["isp"] = isp
        if max_ping_time is not UNSET:
            field_dict["maxPingTime"] = max_ping_time
        if min_ping_time is not UNSET:
            field_dict["minPingTime"] = min_ping_time
        if result is not UNSET:
            field_dict["result"] = result
        if server_details is not UNSET:
            field_dict["serverDetails"] = server_details
        if upload_speed is not UNSET:
            field_dict["uploadSpeed"] = upload_speed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_speedtest_response_200_result_date_time import (
            PostV1DiagnosticSpeedtestResponse200ResultDateTime,
        )
        from ..models.post_v1_diagnostic_speedtest_response_200_result_server_details import (
            PostV1DiagnosticSpeedtestResponse200ResultServerDetails,
        )

        d = src_dict.copy()
        avg_ping_time = d.pop("avgPingTime", UNSET)

        _date_time = d.pop("dateTime", UNSET)
        date_time: Union[Unset, PostV1DiagnosticSpeedtestResponse200ResultDateTime]
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = PostV1DiagnosticSpeedtestResponse200ResultDateTime.from_dict(_date_time)

        download_speed = d.pop("downloadSpeed", UNSET)

        isp = d.pop("isp", UNSET)

        max_ping_time = d.pop("maxPingTime", UNSET)

        min_ping_time = d.pop("minPingTime", UNSET)

        result = d.pop("result", UNSET)

        _server_details = d.pop("serverDetails", UNSET)
        server_details: Union[Unset, PostV1DiagnosticSpeedtestResponse200ResultServerDetails]
        if isinstance(_server_details, Unset):
            server_details = UNSET
        else:
            server_details = PostV1DiagnosticSpeedtestResponse200ResultServerDetails.from_dict(_server_details)

        upload_speed = d.pop("uploadSpeed", UNSET)

        post_v1_diagnostic_speedtest_response_200_result = cls(
            avg_ping_time=avg_ping_time,
            date_time=date_time,
            download_speed=download_speed,
            isp=isp,
            max_ping_time=max_ping_time,
            min_ping_time=min_ping_time,
            result=result,
            server_details=server_details,
            upload_speed=upload_speed,
        )

        post_v1_diagnostic_speedtest_response_200_result.additional_properties = d
        return post_v1_diagnostic_speedtest_response_200_result

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
