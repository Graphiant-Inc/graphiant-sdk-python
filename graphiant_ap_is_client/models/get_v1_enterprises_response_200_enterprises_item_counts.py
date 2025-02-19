from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1EnterprisesResponse200EnterprisesItemCounts")


@_attrs_define
class GetV1EnterprisesResponse200EnterprisesItemCounts:
    """
    Attributes:
        active_down_count (Union[Unset, str]):  Example: TYPE_INT64.
        active_up_count (Union[Unset, str]):  Example: TYPE_INT64.
        deactivated_down_count (Union[Unset, str]):  Example: TYPE_INT64.
        down_sites_count (Union[Unset, str]):  Example: TYPE_INT64.
        empty_sites_count (Union[Unset, str]):  Example: TYPE_INT64.
        impaired_sites_count (Union[Unset, str]):  Example: TYPE_INT64.
        staging_down_count (Union[Unset, str]):  Example: TYPE_INT64.
        staging_up_count (Union[Unset, str]):  Example: TYPE_INT64.
        total_customers (Union[Unset, str]):  Example: TYPE_INT64.
        total_edges (Union[Unset, str]):  Example: TYPE_INT64.
        total_msps (Union[Unset, str]):  Example: TYPE_INT64.
        total_sites (Union[Unset, str]):  Example: TYPE_INT64.
        up_sites_count (Union[Unset, str]):  Example: TYPE_INT64.
    """

    active_down_count: Union[Unset, str] = UNSET
    active_up_count: Union[Unset, str] = UNSET
    deactivated_down_count: Union[Unset, str] = UNSET
    down_sites_count: Union[Unset, str] = UNSET
    empty_sites_count: Union[Unset, str] = UNSET
    impaired_sites_count: Union[Unset, str] = UNSET
    staging_down_count: Union[Unset, str] = UNSET
    staging_up_count: Union[Unset, str] = UNSET
    total_customers: Union[Unset, str] = UNSET
    total_edges: Union[Unset, str] = UNSET
    total_msps: Union[Unset, str] = UNSET
    total_sites: Union[Unset, str] = UNSET
    up_sites_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_down_count = self.active_down_count

        active_up_count = self.active_up_count

        deactivated_down_count = self.deactivated_down_count

        down_sites_count = self.down_sites_count

        empty_sites_count = self.empty_sites_count

        impaired_sites_count = self.impaired_sites_count

        staging_down_count = self.staging_down_count

        staging_up_count = self.staging_up_count

        total_customers = self.total_customers

        total_edges = self.total_edges

        total_msps = self.total_msps

        total_sites = self.total_sites

        up_sites_count = self.up_sites_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_down_count is not UNSET:
            field_dict["activeDownCount"] = active_down_count
        if active_up_count is not UNSET:
            field_dict["activeUpCount"] = active_up_count
        if deactivated_down_count is not UNSET:
            field_dict["deactivatedDownCount"] = deactivated_down_count
        if down_sites_count is not UNSET:
            field_dict["downSitesCount"] = down_sites_count
        if empty_sites_count is not UNSET:
            field_dict["emptySitesCount"] = empty_sites_count
        if impaired_sites_count is not UNSET:
            field_dict["impairedSitesCount"] = impaired_sites_count
        if staging_down_count is not UNSET:
            field_dict["stagingDownCount"] = staging_down_count
        if staging_up_count is not UNSET:
            field_dict["stagingUpCount"] = staging_up_count
        if total_customers is not UNSET:
            field_dict["totalCustomers"] = total_customers
        if total_edges is not UNSET:
            field_dict["totalEdges"] = total_edges
        if total_msps is not UNSET:
            field_dict["totalMsps"] = total_msps
        if total_sites is not UNSET:
            field_dict["totalSites"] = total_sites
        if up_sites_count is not UNSET:
            field_dict["upSitesCount"] = up_sites_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        active_down_count = d.pop("activeDownCount", UNSET)

        active_up_count = d.pop("activeUpCount", UNSET)

        deactivated_down_count = d.pop("deactivatedDownCount", UNSET)

        down_sites_count = d.pop("downSitesCount", UNSET)

        empty_sites_count = d.pop("emptySitesCount", UNSET)

        impaired_sites_count = d.pop("impairedSitesCount", UNSET)

        staging_down_count = d.pop("stagingDownCount", UNSET)

        staging_up_count = d.pop("stagingUpCount", UNSET)

        total_customers = d.pop("totalCustomers", UNSET)

        total_edges = d.pop("totalEdges", UNSET)

        total_msps = d.pop("totalMsps", UNSET)

        total_sites = d.pop("totalSites", UNSET)

        up_sites_count = d.pop("upSitesCount", UNSET)

        get_v1_enterprises_response_200_enterprises_item_counts = cls(
            active_down_count=active_down_count,
            active_up_count=active_up_count,
            deactivated_down_count=deactivated_down_count,
            down_sites_count=down_sites_count,
            empty_sites_count=empty_sites_count,
            impaired_sites_count=impaired_sites_count,
            staging_down_count=staging_down_count,
            staging_up_count=staging_up_count,
            total_customers=total_customers,
            total_edges=total_edges,
            total_msps=total_msps,
            total_sites=total_sites,
            up_sites_count=up_sites_count,
        )

        get_v1_enterprises_response_200_enterprises_item_counts.additional_properties = d
        return get_v1_enterprises_response_200_enterprises_item_counts

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
