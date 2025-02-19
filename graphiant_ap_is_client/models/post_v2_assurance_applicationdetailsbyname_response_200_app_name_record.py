from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_applicationdetailsbyname_response_200_app_name_record_app_id_records_item import (
        PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem,
    )


T = TypeVar("T", bound="PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecord")


@_attrs_define
class PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecord:
    """
    Attributes:
        affected_hosts (Union[Unset, str]):  Example: TYPE_INT64.
        affected_regions (Union[Unset, str]):  Example: TYPE_INT64.
        affected_sites (Union[Unset, str]):  Example: TYPE_INT64.
        affected_vrfs (Union[Unset, str]):  Example: TYPE_INT64.
        app_id_records (Union[Unset,
            list['PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem']]):
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        category (Union[Unset, str]):  Example: TYPE_STRING.
        flows_analyzed (Union[Unset, str]):  Example: TYPE_INT64.
        recommendation (Union[Unset, str]):  Example: TYPE_STRING.
        risk_status (Union[Unset, str]):  Example: TYPE_ENUM.
        threat_score (Union[Unset, str]):  Example: TYPE_INT64.
    """

    affected_hosts: Union[Unset, str] = UNSET
    affected_regions: Union[Unset, str] = UNSET
    affected_sites: Union[Unset, str] = UNSET
    affected_vrfs: Union[Unset, str] = UNSET
    app_id_records: Union[
        Unset, list["PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem"]
    ] = UNSET
    app_name: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    flows_analyzed: Union[Unset, str] = UNSET
    recommendation: Union[Unset, str] = UNSET
    risk_status: Union[Unset, str] = UNSET
    threat_score: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_hosts = self.affected_hosts

        affected_regions = self.affected_regions

        affected_sites = self.affected_sites

        affected_vrfs = self.affected_vrfs

        app_id_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_id_records, Unset):
            app_id_records = []
            for app_id_records_item_data in self.app_id_records:
                app_id_records_item = app_id_records_item_data.to_dict()
                app_id_records.append(app_id_records_item)

        app_name = self.app_name

        category = self.category

        flows_analyzed = self.flows_analyzed

        recommendation = self.recommendation

        risk_status = self.risk_status

        threat_score = self.threat_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_hosts is not UNSET:
            field_dict["affectedHosts"] = affected_hosts
        if affected_regions is not UNSET:
            field_dict["affectedRegions"] = affected_regions
        if affected_sites is not UNSET:
            field_dict["affectedSites"] = affected_sites
        if affected_vrfs is not UNSET:
            field_dict["affectedVrfs"] = affected_vrfs
        if app_id_records is not UNSET:
            field_dict["appIdRecords"] = app_id_records
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if category is not UNSET:
            field_dict["category"] = category
        if flows_analyzed is not UNSET:
            field_dict["flowsAnalyzed"] = flows_analyzed
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if risk_status is not UNSET:
            field_dict["riskStatus"] = risk_status
        if threat_score is not UNSET:
            field_dict["threatScore"] = threat_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_applicationdetailsbyname_response_200_app_name_record_app_id_records_item import (
            PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem,
        )

        d = src_dict.copy()
        affected_hosts = d.pop("affectedHosts", UNSET)

        affected_regions = d.pop("affectedRegions", UNSET)

        affected_sites = d.pop("affectedSites", UNSET)

        affected_vrfs = d.pop("affectedVrfs", UNSET)

        app_id_records = []
        _app_id_records = d.pop("appIdRecords", UNSET)
        for app_id_records_item_data in _app_id_records or []:
            app_id_records_item = (
                PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem.from_dict(
                    app_id_records_item_data
                )
            )

            app_id_records.append(app_id_records_item)

        app_name = d.pop("appName", UNSET)

        category = d.pop("category", UNSET)

        flows_analyzed = d.pop("flowsAnalyzed", UNSET)

        recommendation = d.pop("recommendation", UNSET)

        risk_status = d.pop("riskStatus", UNSET)

        threat_score = d.pop("threatScore", UNSET)

        post_v2_assurance_applicationdetailsbyname_response_200_app_name_record = cls(
            affected_hosts=affected_hosts,
            affected_regions=affected_regions,
            affected_sites=affected_sites,
            affected_vrfs=affected_vrfs,
            app_id_records=app_id_records,
            app_name=app_name,
            category=category,
            flows_analyzed=flows_analyzed,
            recommendation=recommendation,
            risk_status=risk_status,
            threat_score=threat_score,
        )

        post_v2_assurance_applicationdetailsbyname_response_200_app_name_record.additional_properties = d
        return post_v2_assurance_applicationdetailsbyname_response_200_app_name_record

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
