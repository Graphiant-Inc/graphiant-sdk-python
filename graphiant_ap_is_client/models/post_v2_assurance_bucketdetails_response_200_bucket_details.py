from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details_app_id_records_item import (
        PostV2AssuranceBucketdetailsResponse200BucketDetailsAppIdRecordsItem,
    )
    from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details_app_name_records_item import (
        PostV2AssuranceBucketdetailsResponse200BucketDetailsAppNameRecordsItem,
    )
    from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details_trend_value_list_item import (
        PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem,
    )


T = TypeVar("T", bound="PostV2AssuranceBucketdetailsResponse200BucketDetails")


@_attrs_define
class PostV2AssuranceBucketdetailsResponse200BucketDetails:
    """
    Attributes:
        app_count_threat_high (Union[Unset, str]):  Example: TYPE_INT64.
        app_count_threat_low (Union[Unset, str]):  Example: TYPE_INT64.
        app_count_threat_medium (Union[Unset, str]):  Example: TYPE_INT64.
        app_id_records (Union[Unset, list['PostV2AssuranceBucketdetailsResponse200BucketDetailsAppIdRecordsItem']]):
        app_name_records (Union[Unset, list['PostV2AssuranceBucketdetailsResponse200BucketDetailsAppNameRecordsItem']]):
        bucket_name_to_display (Union[Unset, str]):  Example: TYPE_STRING.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        display_ip_port (Union[Unset, str]):  Example: TYPE_BOOL.
        flow_count (Union[Unset, str]):  Example: TYPE_INT64.
        new_ip_hint (Union[Unset, str]):  Example: TYPE_BOOL.
        recommendation (Union[Unset, str]):  Example: TYPE_STRING.
        trend_value_list (Union[Unset, list['PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem']]):
        unique_app_count (Union[Unset, str]):  Example: TYPE_INT64.
    """

    app_count_threat_high: Union[Unset, str] = UNSET
    app_count_threat_low: Union[Unset, str] = UNSET
    app_count_threat_medium: Union[Unset, str] = UNSET
    app_id_records: Union[Unset, list["PostV2AssuranceBucketdetailsResponse200BucketDetailsAppIdRecordsItem"]] = UNSET
    app_name_records: Union[Unset, list["PostV2AssuranceBucketdetailsResponse200BucketDetailsAppNameRecordsItem"]] = (
        UNSET
    )
    bucket_name_to_display: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_ip_port: Union[Unset, str] = UNSET
    flow_count: Union[Unset, str] = UNSET
    new_ip_hint: Union[Unset, str] = UNSET
    recommendation: Union[Unset, str] = UNSET
    trend_value_list: Union[Unset, list["PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem"]] = (
        UNSET
    )
    unique_app_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_count_threat_high = self.app_count_threat_high

        app_count_threat_low = self.app_count_threat_low

        app_count_threat_medium = self.app_count_threat_medium

        app_id_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_id_records, Unset):
            app_id_records = []
            for app_id_records_item_data in self.app_id_records:
                app_id_records_item = app_id_records_item_data.to_dict()
                app_id_records.append(app_id_records_item)

        app_name_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_name_records, Unset):
            app_name_records = []
            for app_name_records_item_data in self.app_name_records:
                app_name_records_item = app_name_records_item_data.to_dict()
                app_name_records.append(app_name_records_item)

        bucket_name_to_display = self.bucket_name_to_display

        description = self.description

        display_ip_port = self.display_ip_port

        flow_count = self.flow_count

        new_ip_hint = self.new_ip_hint

        recommendation = self.recommendation

        trend_value_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.trend_value_list, Unset):
            trend_value_list = []
            for trend_value_list_item_data in self.trend_value_list:
                trend_value_list_item = trend_value_list_item_data.to_dict()
                trend_value_list.append(trend_value_list_item)

        unique_app_count = self.unique_app_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_count_threat_high is not UNSET:
            field_dict["appCountThreatHigh"] = app_count_threat_high
        if app_count_threat_low is not UNSET:
            field_dict["appCountThreatLow"] = app_count_threat_low
        if app_count_threat_medium is not UNSET:
            field_dict["appCountThreatMedium"] = app_count_threat_medium
        if app_id_records is not UNSET:
            field_dict["appIdRecords"] = app_id_records
        if app_name_records is not UNSET:
            field_dict["appNameRecords"] = app_name_records
        if bucket_name_to_display is not UNSET:
            field_dict["bucketNameToDisplay"] = bucket_name_to_display
        if description is not UNSET:
            field_dict["description"] = description
        if display_ip_port is not UNSET:
            field_dict["displayIpPort"] = display_ip_port
        if flow_count is not UNSET:
            field_dict["flowCount"] = flow_count
        if new_ip_hint is not UNSET:
            field_dict["newIpHint"] = new_ip_hint
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if trend_value_list is not UNSET:
            field_dict["trendValueList"] = trend_value_list
        if unique_app_count is not UNSET:
            field_dict["uniqueAppCount"] = unique_app_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details_app_id_records_item import (
            PostV2AssuranceBucketdetailsResponse200BucketDetailsAppIdRecordsItem,
        )
        from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details_app_name_records_item import (
            PostV2AssuranceBucketdetailsResponse200BucketDetailsAppNameRecordsItem,
        )
        from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details_trend_value_list_item import (
            PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem,
        )

        d = src_dict.copy()
        app_count_threat_high = d.pop("appCountThreatHigh", UNSET)

        app_count_threat_low = d.pop("appCountThreatLow", UNSET)

        app_count_threat_medium = d.pop("appCountThreatMedium", UNSET)

        app_id_records = []
        _app_id_records = d.pop("appIdRecords", UNSET)
        for app_id_records_item_data in _app_id_records or []:
            app_id_records_item = PostV2AssuranceBucketdetailsResponse200BucketDetailsAppIdRecordsItem.from_dict(
                app_id_records_item_data
            )

            app_id_records.append(app_id_records_item)

        app_name_records = []
        _app_name_records = d.pop("appNameRecords", UNSET)
        for app_name_records_item_data in _app_name_records or []:
            app_name_records_item = PostV2AssuranceBucketdetailsResponse200BucketDetailsAppNameRecordsItem.from_dict(
                app_name_records_item_data
            )

            app_name_records.append(app_name_records_item)

        bucket_name_to_display = d.pop("bucketNameToDisplay", UNSET)

        description = d.pop("description", UNSET)

        display_ip_port = d.pop("displayIpPort", UNSET)

        flow_count = d.pop("flowCount", UNSET)

        new_ip_hint = d.pop("newIpHint", UNSET)

        recommendation = d.pop("recommendation", UNSET)

        trend_value_list = []
        _trend_value_list = d.pop("trendValueList", UNSET)
        for trend_value_list_item_data in _trend_value_list or []:
            trend_value_list_item = PostV2AssuranceBucketdetailsResponse200BucketDetailsTrendValueListItem.from_dict(
                trend_value_list_item_data
            )

            trend_value_list.append(trend_value_list_item)

        unique_app_count = d.pop("uniqueAppCount", UNSET)

        post_v2_assurance_bucketdetails_response_200_bucket_details = cls(
            app_count_threat_high=app_count_threat_high,
            app_count_threat_low=app_count_threat_low,
            app_count_threat_medium=app_count_threat_medium,
            app_id_records=app_id_records,
            app_name_records=app_name_records,
            bucket_name_to_display=bucket_name_to_display,
            description=description,
            display_ip_port=display_ip_port,
            flow_count=flow_count,
            new_ip_hint=new_ip_hint,
            recommendation=recommendation,
            trend_value_list=trend_value_list,
            unique_app_count=unique_app_count,
        )

        post_v2_assurance_bucketdetails_response_200_bucket_details.additional_properties = d
        return post_v2_assurance_bucketdetails_response_200_bucket_details

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
