from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_sites_response_200_site import PostV1SitesResponse200Site


T = TypeVar("T", bound="PostV1SitesResponse200")


@_attrs_define
class PostV1SitesResponse200:
    """
    Attributes:
        site (Union[Unset, PostV1SitesResponse200Site]):
    """

    site: Union[Unset, "PostV1SitesResponse200Site"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_sites_response_200_site import PostV1SitesResponse200Site

        d = src_dict.copy()
        _site = d.pop("site", UNSET)
        site: Union[Unset, PostV1SitesResponse200Site]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PostV1SitesResponse200Site.from_dict(_site)

        post_v1_sites_response_200 = cls(
            site=site,
        )

        post_v1_sites_response_200.additional_properties = d
        return post_v1_sites_response_200

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
