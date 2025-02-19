from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem")


@_attrs_define
class GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_INT64.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        kind (Union[Unset, str]):  Example: TYPE_ENUM.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    app_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        description = self.description

        kind = self.kind

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        description = d.pop("description", UNSET)

        kind = d.pop("kind", UNSET)

        name = d.pop("name", UNSET)

        get_v1_devices_device_id_policy_applications_response_200_applications_item = cls(
            app_id=app_id,
            description=description,
            kind=kind,
            name=name,
        )

        get_v1_devices_device_id_policy_applications_response_200_applications_item.additional_properties = d
        return get_v1_devices_device_id_policy_applications_response_200_applications_item

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
