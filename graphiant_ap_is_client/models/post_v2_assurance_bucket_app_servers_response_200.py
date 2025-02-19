from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_bucket_app_servers_response_200_app_servers_item import (
        PostV2AssuranceBucketAppServersResponse200AppServersItem,
    )


T = TypeVar("T", bound="PostV2AssuranceBucketAppServersResponse200")


@_attrs_define
class PostV2AssuranceBucketAppServersResponse200:
    """
    Attributes:
        app_servers (Union[Unset, list['PostV2AssuranceBucketAppServersResponse200AppServersItem']]):
    """

    app_servers: Union[Unset, list["PostV2AssuranceBucketAppServersResponse200AppServersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_servers, Unset):
            app_servers = []
            for app_servers_item_data in self.app_servers:
                app_servers_item = app_servers_item_data.to_dict()
                app_servers.append(app_servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_servers is not UNSET:
            field_dict["appServers"] = app_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_bucket_app_servers_response_200_app_servers_item import (
            PostV2AssuranceBucketAppServersResponse200AppServersItem,
        )

        d = src_dict.copy()
        app_servers = []
        _app_servers = d.pop("appServers", UNSET)
        for app_servers_item_data in _app_servers or []:
            app_servers_item = PostV2AssuranceBucketAppServersResponse200AppServersItem.from_dict(app_servers_item_data)

            app_servers.append(app_servers_item)

        post_v2_assurance_bucket_app_servers_response_200 = cls(
            app_servers=app_servers,
        )

        post_v2_assurance_bucket_app_servers_response_200.additional_properties = d
        return post_v2_assurance_bucket_app_servers_response_200

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
