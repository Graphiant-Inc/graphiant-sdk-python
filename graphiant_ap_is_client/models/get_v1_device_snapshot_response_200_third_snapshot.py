from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_snapshot_response_200_third_snapshot_author import (
        GetV1DeviceSnapshotResponse200ThirdSnapshotAuthor,
    )
    from ..models.get_v1_device_snapshot_response_200_third_snapshot_created_on import (
        GetV1DeviceSnapshotResponse200ThirdSnapshotCreatedOn,
    )
    from ..models.get_v1_device_snapshot_response_200_third_snapshot_data import (
        GetV1DeviceSnapshotResponse200ThirdSnapshotData,
    )


T = TypeVar("T", bound="GetV1DeviceSnapshotResponse200ThirdSnapshot")


@_attrs_define
class GetV1DeviceSnapshotResponse200ThirdSnapshot:
    """
    Attributes:
        author (Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshotAuthor]):
        category (Union[Unset, str]):  Example: TYPE_ENUM.
        created_on (Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshotCreatedOn]):
        data (Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshotData]):
        golden (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: 6-1-24-status-check.
    """

    author: Union[Unset, "GetV1DeviceSnapshotResponse200ThirdSnapshotAuthor"] = UNSET
    category: Union[Unset, str] = UNSET
    created_on: Union[Unset, "GetV1DeviceSnapshotResponse200ThirdSnapshotCreatedOn"] = UNSET
    data: Union[Unset, "GetV1DeviceSnapshotResponse200ThirdSnapshotData"] = UNSET
    golden: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        category = self.category

        created_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        golden = self.golden

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if category is not UNSET:
            field_dict["category"] = category
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if data is not UNSET:
            field_dict["data"] = data
        if golden is not UNSET:
            field_dict["golden"] = golden
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_snapshot_response_200_third_snapshot_author import (
            GetV1DeviceSnapshotResponse200ThirdSnapshotAuthor,
        )
        from ..models.get_v1_device_snapshot_response_200_third_snapshot_created_on import (
            GetV1DeviceSnapshotResponse200ThirdSnapshotCreatedOn,
        )
        from ..models.get_v1_device_snapshot_response_200_third_snapshot_data import (
            GetV1DeviceSnapshotResponse200ThirdSnapshotData,
        )

        d = src_dict.copy()
        _author = d.pop("author", UNSET)
        author: Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshotAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = GetV1DeviceSnapshotResponse200ThirdSnapshotAuthor.from_dict(_author)

        category = d.pop("category", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshotCreatedOn]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = GetV1DeviceSnapshotResponse200ThirdSnapshotCreatedOn.from_dict(_created_on)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GetV1DeviceSnapshotResponse200ThirdSnapshotData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetV1DeviceSnapshotResponse200ThirdSnapshotData.from_dict(_data)

        golden = d.pop("golden", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_v1_device_snapshot_response_200_third_snapshot = cls(
            author=author,
            category=category,
            created_on=created_on,
            data=data,
            golden=golden,
            id=id,
            name=name,
        )

        get_v1_device_snapshot_response_200_third_snapshot.additional_properties = d
        return get_v1_device_snapshot_response_200_third_snapshot

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
