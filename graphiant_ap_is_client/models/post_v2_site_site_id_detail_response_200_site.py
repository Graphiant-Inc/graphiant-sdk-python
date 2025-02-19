from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2SiteSiteIdDetailResponse200Site")


@_attrs_define
class PostV2SiteSiteIdDetailResponse200Site:
    """
    Attributes:
        status (Union[Unset, str]):  Example: TYPE_STRING.
        total_applications (Union[Unset, str]):  Example: TYPE_INT64.
        total_circuits (Union[Unset, str]):  Example: TYPE_INT64.
        total_edges (Union[Unset, str]):  Example: TYPE_INT64.
    """

    status: Union[Unset, str] = UNSET
    total_applications: Union[Unset, str] = UNSET
    total_circuits: Union[Unset, str] = UNSET
    total_edges: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        total_applications = self.total_applications

        total_circuits = self.total_circuits

        total_edges = self.total_edges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if total_applications is not UNSET:
            field_dict["totalApplications"] = total_applications
        if total_circuits is not UNSET:
            field_dict["totalCircuits"] = total_circuits
        if total_edges is not UNSET:
            field_dict["totalEdges"] = total_edges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        total_applications = d.pop("totalApplications", UNSET)

        total_circuits = d.pop("totalCircuits", UNSET)

        total_edges = d.pop("totalEdges", UNSET)

        post_v2_site_site_id_detail_response_200_site = cls(
            status=status,
            total_applications=total_applications,
            total_circuits=total_circuits,
            total_edges=total_edges,
        )

        post_v2_site_site_id_detail_response_200_site.additional_properties = d
        return post_v2_site_site_id_detail_response_200_site

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
