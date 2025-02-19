from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_overview_body_dimensions import PostV1BackboneHealthOverviewBodyDimensions
    from ..models.post_v1_backbone_health_overview_body_filter import PostV1BackboneHealthOverviewBodyFilter


T = TypeVar("T", bound="PostV1BackboneHealthOverviewBody")


@_attrs_define
class PostV1BackboneHealthOverviewBody:
    """
    Attributes:
        dimensions (Union[Unset, PostV1BackboneHealthOverviewBodyDimensions]):
        filter_ (Union[Unset, PostV1BackboneHealthOverviewBodyFilter]):
    """

    dimensions: Union[Unset, "PostV1BackboneHealthOverviewBodyDimensions"] = UNSET
    filter_: Union[Unset, "PostV1BackboneHealthOverviewBodyFilter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimensions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_overview_body_dimensions import PostV1BackboneHealthOverviewBodyDimensions
        from ..models.post_v1_backbone_health_overview_body_filter import PostV1BackboneHealthOverviewBodyFilter

        d = src_dict.copy()
        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, PostV1BackboneHealthOverviewBodyDimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = PostV1BackboneHealthOverviewBodyDimensions.from_dict(_dimensions)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, PostV1BackboneHealthOverviewBodyFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostV1BackboneHealthOverviewBodyFilter.from_dict(_filter_)

        post_v1_backbone_health_overview_body = cls(
            dimensions=dimensions,
            filter_=filter_,
        )

        post_v1_backbone_health_overview_body.additional_properties = d
        return post_v1_backbone_health_overview_body

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
