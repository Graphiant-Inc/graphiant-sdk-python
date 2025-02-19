from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item_author_permissions import (
        GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthorPermissions,
    )


T = TypeVar("T", bound="GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthor")


@_attrs_define
class GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthor:
    """
    Attributes:
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        exp (Union[Unset, str]):  Example: TYPE_INT64.
        original_enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        permissions (Union[Unset,
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthorPermissions]):
        time_zone (Union[Unset, str]):  Example: TYPE_STRING.
        user_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    enterprise_id: Union[Unset, str] = UNSET
    exp: Union[Unset, str] = UNSET
    original_enterprise_id: Union[Unset, str] = UNSET
    permissions: Union[
        Unset, "GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthorPermissions"
    ] = UNSET
    time_zone: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enterprise_id = self.enterprise_id

        exp = self.exp

        original_enterprise_id = self.original_enterprise_id

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        time_zone = self.time_zone

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if exp is not UNSET:
            field_dict["exp"] = exp
        if original_enterprise_id is not UNSET:
            field_dict["originalEnterpriseId"] = original_enterprise_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item_author_permissions import (
            GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthorPermissions,
        )

        d = src_dict.copy()
        enterprise_id = d.pop("enterpriseId", UNSET)

        exp = d.pop("exp", UNSET)

        original_enterprise_id = d.pop("originalEnterpriseId", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[
            Unset, GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthorPermissions
        ]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = (
                GetV1EnterpriseSnapshotResponse200DeviceSnapshotRecordsItemSnapshotsItemAuthorPermissions.from_dict(
                    _permissions
                )
            )

        time_zone = d.pop("timeZone", UNSET)

        user_id = d.pop("userId", UNSET)

        get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item_author = cls(
            enterprise_id=enterprise_id,
            exp=exp,
            original_enterprise_id=original_enterprise_id,
            permissions=permissions,
            time_zone=time_zone,
            user_id=user_id,
        )

        get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item_author.additional_properties = d
        return get_v1_enterprise_snapshot_response_200_device_snapshot_records_item_snapshots_item_author

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
