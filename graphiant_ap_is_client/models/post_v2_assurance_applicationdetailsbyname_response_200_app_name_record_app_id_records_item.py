from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem")


@_attrs_define
class PostV2AssuranceApplicationdetailsbynameResponse200AppNameRecordAppIdRecordsItem:
    """
    Attributes:
        affected_hosts (Union[Unset, str]):  Example: TYPE_INT64.
        affected_regions (Union[Unset, str]):  Example: TYPE_INT64.
        affected_sites (Union[Unset, str]):  Example: TYPE_INT64.
        affected_vrfs (Union[Unset, str]):  Example: TYPE_INT64.
        app_id_key (Union[Unset, str]):  Example: TYPE_STRING.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        blocked_reason_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        category (Union[Unset, str]):  Example: TYPE_STRING.
        classfication_field (Union[Unset, str]):  Example: TYPE_STRING.
        classification_field (Union[Unset, str]):  Example: TYPE_STRING.
        first_seen (Union[Unset, str]):  Example: TYPE_INT64.
        flows_analyzed (Union[Unset, str]):  Example: TYPE_INT64.
        last_seen (Union[Unset, str]):  Example: TYPE_INT64.
        new_ip_hint (Union[Unset, str]):  Example: TYPE_BOOL.
        recommendation (Union[Unset, str]):  Example: TYPE_STRING.
        region_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        risk_status (Union[Unset, str]):  Example: TYPE_ENUM.
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_port (Union[Unset, str]):  Example: TYPE_STRING.
        site_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        threat_score (Union[Unset, str]):  Example: TYPE_INT64.
        vrf_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    affected_hosts: Union[Unset, str] = UNSET
    affected_regions: Union[Unset, str] = UNSET
    affected_sites: Union[Unset, str] = UNSET
    affected_vrfs: Union[Unset, str] = UNSET
    app_id_key: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    blocked_reason_list: Union[Unset, list[str]] = UNSET
    category: Union[Unset, str] = UNSET
    classfication_field: Union[Unset, str] = UNSET
    classification_field: Union[Unset, str] = UNSET
    first_seen: Union[Unset, str] = UNSET
    flows_analyzed: Union[Unset, str] = UNSET
    last_seen: Union[Unset, str] = UNSET
    new_ip_hint: Union[Unset, str] = UNSET
    recommendation: Union[Unset, str] = UNSET
    region_list: Union[Unset, list[str]] = UNSET
    risk_status: Union[Unset, str] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    site_list: Union[Unset, list[str]] = UNSET
    threat_score: Union[Unset, str] = UNSET
    vrf_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_hosts = self.affected_hosts

        affected_regions = self.affected_regions

        affected_sites = self.affected_sites

        affected_vrfs = self.affected_vrfs

        app_id_key = self.app_id_key

        app_name = self.app_name

        blocked_reason_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.blocked_reason_list, Unset):
            blocked_reason_list = self.blocked_reason_list

        category = self.category

        classfication_field = self.classfication_field

        classification_field = self.classification_field

        first_seen = self.first_seen

        flows_analyzed = self.flows_analyzed

        last_seen = self.last_seen

        new_ip_hint = self.new_ip_hint

        recommendation = self.recommendation

        region_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.region_list, Unset):
            region_list = self.region_list

        risk_status = self.risk_status

        server_ip = self.server_ip

        server_port = self.server_port

        site_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.site_list, Unset):
            site_list = self.site_list

        threat_score = self.threat_score

        vrf_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vrf_list, Unset):
            vrf_list = self.vrf_list

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
        if app_id_key is not UNSET:
            field_dict["appIdKey"] = app_id_key
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if blocked_reason_list is not UNSET:
            field_dict["blockedReasonList"] = blocked_reason_list
        if category is not UNSET:
            field_dict["category"] = category
        if classfication_field is not UNSET:
            field_dict["classficationField"] = classfication_field
        if classification_field is not UNSET:
            field_dict["classificationField"] = classification_field
        if first_seen is not UNSET:
            field_dict["firstSeen"] = first_seen
        if flows_analyzed is not UNSET:
            field_dict["flowsAnalyzed"] = flows_analyzed
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if new_ip_hint is not UNSET:
            field_dict["newIpHint"] = new_ip_hint
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if region_list is not UNSET:
            field_dict["regionList"] = region_list
        if risk_status is not UNSET:
            field_dict["riskStatus"] = risk_status
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if site_list is not UNSET:
            field_dict["siteList"] = site_list
        if threat_score is not UNSET:
            field_dict["threatScore"] = threat_score
        if vrf_list is not UNSET:
            field_dict["vrfList"] = vrf_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        affected_hosts = d.pop("affectedHosts", UNSET)

        affected_regions = d.pop("affectedRegions", UNSET)

        affected_sites = d.pop("affectedSites", UNSET)

        affected_vrfs = d.pop("affectedVrfs", UNSET)

        app_id_key = d.pop("appIdKey", UNSET)

        app_name = d.pop("appName", UNSET)

        blocked_reason_list = cast(list[str], d.pop("blockedReasonList", UNSET))

        category = d.pop("category", UNSET)

        classfication_field = d.pop("classficationField", UNSET)

        classification_field = d.pop("classificationField", UNSET)

        first_seen = d.pop("firstSeen", UNSET)

        flows_analyzed = d.pop("flowsAnalyzed", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        new_ip_hint = d.pop("newIpHint", UNSET)

        recommendation = d.pop("recommendation", UNSET)

        region_list = cast(list[str], d.pop("regionList", UNSET))

        risk_status = d.pop("riskStatus", UNSET)

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        site_list = cast(list[str], d.pop("siteList", UNSET))

        threat_score = d.pop("threatScore", UNSET)

        vrf_list = cast(list[str], d.pop("vrfList", UNSET))

        post_v2_assurance_applicationdetailsbyname_response_200_app_name_record_app_id_records_item = cls(
            affected_hosts=affected_hosts,
            affected_regions=affected_regions,
            affected_sites=affected_sites,
            affected_vrfs=affected_vrfs,
            app_id_key=app_id_key,
            app_name=app_name,
            blocked_reason_list=blocked_reason_list,
            category=category,
            classfication_field=classfication_field,
            classification_field=classification_field,
            first_seen=first_seen,
            flows_analyzed=flows_analyzed,
            last_seen=last_seen,
            new_ip_hint=new_ip_hint,
            recommendation=recommendation,
            region_list=region_list,
            risk_status=risk_status,
            server_ip=server_ip,
            server_port=server_port,
            site_list=site_list,
            threat_score=threat_score,
            vrf_list=vrf_list,
        )

        post_v2_assurance_applicationdetailsbyname_response_200_app_name_record_app_id_records_item.additional_properties = d
        return post_v2_assurance_applicationdetailsbyname_response_200_app_name_record_app_id_records_item

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
