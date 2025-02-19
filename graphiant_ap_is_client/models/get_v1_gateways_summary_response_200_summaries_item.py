from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_summary_response_200_summaries_item_created_at import (
        GetV1GatewaysSummaryResponse200SummariesItemCreatedAt,
    )
    from ..models.get_v1_gateways_summary_response_200_summaries_item_gateway_device_summary_item import (
        GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem,
    )
    from ..models.get_v1_gateways_summary_response_200_summaries_item_updated_at import (
        GetV1GatewaysSummaryResponse200SummariesItemUpdatedAt,
    )


T = TypeVar("T", bound="GetV1GatewaysSummaryResponse200SummariesItem")


@_attrs_define
class GetV1GatewaysSummaryResponse200SummariesItem:
    """
    Attributes:
        created_at (Union[Unset, GetV1GatewaysSummaryResponse200SummariesItemCreatedAt]):
        gateway_device_summary (Union[Unset,
            list['GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem']]):
        graphiant_region (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        speed (Union[Unset, str]):  Example: TYPE_ENUM.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        support_status (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
        updated_at (Union[Unset, GetV1GatewaysSummaryResponse200SummariesItemUpdatedAt]):
    """

    created_at: Union[Unset, "GetV1GatewaysSummaryResponse200SummariesItemCreatedAt"] = UNSET
    gateway_device_summary: Union[
        Unset, list["GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem"]
    ] = UNSET
    graphiant_region: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    support_status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, "GetV1GatewaysSummaryResponse200SummariesItemUpdatedAt"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        gateway_device_summary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.gateway_device_summary, Unset):
            gateway_device_summary = []
            for gateway_device_summary_item_data in self.gateway_device_summary:
                gateway_device_summary_item = gateway_device_summary_item_data.to_dict()
                gateway_device_summary.append(gateway_device_summary_item)

        graphiant_region = self.graphiant_region

        id = self.id

        name = self.name

        speed = self.speed

        status = self.status

        support_status = self.support_status

        type_ = self.type_

        updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if gateway_device_summary is not UNSET:
            field_dict["gatewayDeviceSummary"] = gateway_device_summary
        if graphiant_region is not UNSET:
            field_dict["graphiantRegion"] = graphiant_region
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if speed is not UNSET:
            field_dict["speed"] = speed
        if status is not UNSET:
            field_dict["status"] = status
        if support_status is not UNSET:
            field_dict["supportStatus"] = support_status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_summary_response_200_summaries_item_created_at import (
            GetV1GatewaysSummaryResponse200SummariesItemCreatedAt,
        )
        from ..models.get_v1_gateways_summary_response_200_summaries_item_gateway_device_summary_item import (
            GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem,
        )
        from ..models.get_v1_gateways_summary_response_200_summaries_item_updated_at import (
            GetV1GatewaysSummaryResponse200SummariesItemUpdatedAt,
        )

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1GatewaysSummaryResponse200SummariesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1GatewaysSummaryResponse200SummariesItemCreatedAt.from_dict(_created_at)

        gateway_device_summary = []
        _gateway_device_summary = d.pop("gatewayDeviceSummary", UNSET)
        for gateway_device_summary_item_data in _gateway_device_summary or []:
            gateway_device_summary_item = (
                GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem.from_dict(
                    gateway_device_summary_item_data
                )
            )

            gateway_device_summary.append(gateway_device_summary_item)

        graphiant_region = d.pop("graphiantRegion", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        speed = d.pop("speed", UNSET)

        status = d.pop("status", UNSET)

        support_status = d.pop("supportStatus", UNSET)

        type_ = d.pop("type", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, GetV1GatewaysSummaryResponse200SummariesItemUpdatedAt]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = GetV1GatewaysSummaryResponse200SummariesItemUpdatedAt.from_dict(_updated_at)

        get_v1_gateways_summary_response_200_summaries_item = cls(
            created_at=created_at,
            gateway_device_summary=gateway_device_summary,
            graphiant_region=graphiant_region,
            id=id,
            name=name,
            speed=speed,
            status=status,
            support_status=support_status,
            type_=type_,
            updated_at=updated_at,
        )

        get_v1_gateways_summary_response_200_summaries_item.additional_properties = d
        return get_v1_gateways_summary_response_200_summaries_item

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
