from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_extranet_log_details_response_200_logs_item import (
        PostV2MonitoringExtranetLogDetailsResponse200LogsItem,
    )


T = TypeVar("T", bound="PostV2MonitoringExtranetLogDetailsResponse200")


@_attrs_define
class PostV2MonitoringExtranetLogDetailsResponse200:
    """
    Attributes:
        logs (Union[Unset, list['PostV2MonitoringExtranetLogDetailsResponse200LogsItem']]):
    """

    logs: Union[Unset, list["PostV2MonitoringExtranetLogDetailsResponse200LogsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_extranet_log_details_response_200_logs_item import (
            PostV2MonitoringExtranetLogDetailsResponse200LogsItem,
        )

        d = src_dict.copy()
        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = PostV2MonitoringExtranetLogDetailsResponse200LogsItem.from_dict(logs_item_data)

            logs.append(logs_item)

        post_v2_monitoring_extranet_log_details_response_200 = cls(
            logs=logs,
        )

        post_v2_monitoring_extranet_log_details_response_200.additional_properties = d
        return post_v2_monitoring_extranet_log_details_response_200

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
