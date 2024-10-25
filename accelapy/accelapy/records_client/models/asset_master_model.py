import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_master_model_dependent_flag import AssetMasterModelDependentFlag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_master_model_comments import AssetMasterModelComments
    from ..models.asset_master_model_description import AssetMasterModelDescription
    from ..models.asset_master_model_name import AssetMasterModelName
    from ..models.asset_master_model_status import AssetMasterModelStatus
    from ..models.asset_master_model_type import AssetMasterModelType
    from ..models.gis_object_model import GISObjectModel


T = TypeVar("T", bound="AssetMasterModel")


@_attrs_define
class AssetMasterModel:
    """
    Attributes:
        asset_id (Union[Unset, str]): The unique alpha-numeric asset ID in an asset group.

            **Added in Civic Platform version**: 9.2.0

        class_type (Union[Unset, str]): A Class Type is how Civic Platform groups objects that an agency owns or
            maintains. The five class types are component, linear, node-link linear, point, and polygon. Asset class types
            provide the ability to assign or group multiple asset types together.
        comments (Union[Unset, AssetMasterModelComments]): General comments about the asset.
        current_value (Union[Unset, float]): The current value of the asset.
        date_of_service (Union[Unset, datetime.datetime]): The date the asset was initially placed into service.
        dependent_flag (Union[Unset, AssetMasterModelDependentFlag]): Indicates whether or not the parent asset is
            dependent on this asset.
        depreciation_amount (Union[Unset, float]): The decline in the asset value by the asset depreciation calculation.
        depreciation_end_date (Union[Unset, datetime.datetime]): The end date for the asset depreciation calculation.
            This field is used in the asset depreciation calculation.
        depreciation_start_date (Union[Unset, datetime.datetime]): The start date for the asset depreciation
            calculation. This field is used in the asset depreciation calculation.
        depreciation_value (Union[Unset, float]): The asset value after the asset depreciation calculation, which is
            based on the start value, depreciation start and end dates, useful life, and salvage value.
        description (Union[Unset, AssetMasterModelDescription]): The description of the asset.
        end_id (Union[Unset, str]): The ending point asset ID.
        gis_objects (Union[Unset, List['GISObjectModel']]):
        id (Union[Unset, int]): The asset system id assigned by the Civic Platform server.
        name (Union[Unset, AssetMasterModelName]): The descriptive name of the asset.
        number (Union[Unset, str]): The unique, alpha-numeric asset ID.
        salvage_value (Union[Unset, float]): The residual value of the asset at the end of itâ€™s useful life.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        size (Union[Unset, float]): A positive numeric value for the asset size.
        size_unit (Union[Unset, str]): The unit of measure corresponding to the asset size.
        start_id (Union[Unset, str]): The starting point asset ID.
        start_value (Union[Unset, float]): The beginning value or purchase price of the asset.
        status (Union[Unset, AssetMasterModelStatus]): The status of the asset.
        status_date (Union[Unset, datetime.datetime]): The date the asset status changed.
        type (Union[Unset, AssetMasterModelType]): The type of asset.
    """

    asset_id: Union[Unset, str] = UNSET
    class_type: Union[Unset, str] = UNSET
    comments: Union[Unset, "AssetMasterModelComments"] = UNSET
    current_value: Union[Unset, float] = UNSET
    date_of_service: Union[Unset, datetime.datetime] = UNSET
    dependent_flag: Union[Unset, AssetMasterModelDependentFlag] = UNSET
    depreciation_amount: Union[Unset, float] = UNSET
    depreciation_end_date: Union[Unset, datetime.datetime] = UNSET
    depreciation_start_date: Union[Unset, datetime.datetime] = UNSET
    depreciation_value: Union[Unset, float] = UNSET
    description: Union[Unset, "AssetMasterModelDescription"] = UNSET
    end_id: Union[Unset, str] = UNSET
    gis_objects: Union[Unset, List["GISObjectModel"]] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, "AssetMasterModelName"] = UNSET
    number: Union[Unset, str] = UNSET
    salvage_value: Union[Unset, float] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    size_unit: Union[Unset, str] = UNSET
    start_id: Union[Unset, str] = UNSET
    start_value: Union[Unset, float] = UNSET
    status: Union[Unset, "AssetMasterModelStatus"] = UNSET
    status_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, "AssetMasterModelType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id
        class_type = self.class_type
        comments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        current_value = self.current_value
        date_of_service: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_service, Unset):
            date_of_service = self.date_of_service.isoformat()

        dependent_flag: Union[Unset, str] = UNSET
        if not isinstance(self.dependent_flag, Unset):
            dependent_flag = self.dependent_flag.value

        depreciation_amount = self.depreciation_amount
        depreciation_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.depreciation_end_date, Unset):
            depreciation_end_date = self.depreciation_end_date.isoformat()

        depreciation_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.depreciation_start_date, Unset):
            depreciation_start_date = self.depreciation_start_date.isoformat()

        depreciation_value = self.depreciation_value
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        end_id = self.end_id
        gis_objects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gis_objects, Unset):
            gis_objects = []
            for gis_objects_item_data in self.gis_objects:
                gis_objects_item = gis_objects_item_data.to_dict()

                gis_objects.append(gis_objects_item)

        id = self.id
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        number = self.number
        salvage_value = self.salvage_value
        service_provider_code = self.service_provider_code
        size = self.size
        size_unit = self.size_unit
        start_id = self.start_id
        start_value = self.start_value
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if class_type is not UNSET:
            field_dict["classType"] = class_type
        if comments is not UNSET:
            field_dict["comments"] = comments
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if date_of_service is not UNSET:
            field_dict["dateOfService"] = date_of_service
        if dependent_flag is not UNSET:
            field_dict["dependentFlag"] = dependent_flag
        if depreciation_amount is not UNSET:
            field_dict["depreciationAmount"] = depreciation_amount
        if depreciation_end_date is not UNSET:
            field_dict["depreciationEndDate"] = depreciation_end_date
        if depreciation_start_date is not UNSET:
            field_dict["depreciationStartDate"] = depreciation_start_date
        if depreciation_value is not UNSET:
            field_dict["depreciationValue"] = depreciation_value
        if description is not UNSET:
            field_dict["description"] = description
        if end_id is not UNSET:
            field_dict["endID"] = end_id
        if gis_objects is not UNSET:
            field_dict["gisObjects"] = gis_objects
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if salvage_value is not UNSET:
            field_dict["salvageValue"] = salvage_value
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if size is not UNSET:
            field_dict["size"] = size
        if size_unit is not UNSET:
            field_dict["sizeUnit"] = size_unit
        if start_id is not UNSET:
            field_dict["startID"] = start_id
        if start_value is not UNSET:
            field_dict["startValue"] = start_value
        if status is not UNSET:
            field_dict["status"] = status
        if status_date is not UNSET:
            field_dict["statusDate"] = status_date
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_master_model_comments import AssetMasterModelComments
        from ..models.asset_master_model_description import AssetMasterModelDescription
        from ..models.asset_master_model_name import AssetMasterModelName
        from ..models.asset_master_model_status import AssetMasterModelStatus
        from ..models.asset_master_model_type import AssetMasterModelType
        from ..models.gis_object_model import GISObjectModel

        d = src_dict.copy()
        asset_id = d.pop("assetId", UNSET)

        class_type = d.pop("classType", UNSET)

        _comments = d.pop("comments", UNSET)
        comments: Union[Unset, AssetMasterModelComments]
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = AssetMasterModelComments.from_dict(_comments)

        current_value = d.pop("currentValue", UNSET)

        _date_of_service = d.pop("dateOfService", UNSET)
        date_of_service: Union[Unset, datetime.datetime]
        if isinstance(_date_of_service, Unset):
            date_of_service = UNSET
        else:
            date_of_service = isoparse(_date_of_service)

        _dependent_flag = d.pop("dependentFlag", UNSET)
        dependent_flag: Union[Unset, AssetMasterModelDependentFlag]
        if isinstance(_dependent_flag, Unset):
            dependent_flag = UNSET
        else:
            dependent_flag = AssetMasterModelDependentFlag(_dependent_flag)

        depreciation_amount = d.pop("depreciationAmount", UNSET)

        _depreciation_end_date = d.pop("depreciationEndDate", UNSET)
        depreciation_end_date: Union[Unset, datetime.datetime]
        if isinstance(_depreciation_end_date, Unset):
            depreciation_end_date = UNSET
        else:
            depreciation_end_date = isoparse(_depreciation_end_date)

        _depreciation_start_date = d.pop("depreciationStartDate", UNSET)
        depreciation_start_date: Union[Unset, datetime.datetime]
        if isinstance(_depreciation_start_date, Unset):
            depreciation_start_date = UNSET
        else:
            depreciation_start_date = isoparse(_depreciation_start_date)

        depreciation_value = d.pop("depreciationValue", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, AssetMasterModelDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = AssetMasterModelDescription.from_dict(_description)

        end_id = d.pop("endID", UNSET)

        gis_objects = []
        _gis_objects = d.pop("gisObjects", UNSET)
        for gis_objects_item_data in _gis_objects or []:
            gis_objects_item = GISObjectModel.from_dict(gis_objects_item_data)

            gis_objects.append(gis_objects_item)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, AssetMasterModelName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = AssetMasterModelName.from_dict(_name)

        number = d.pop("number", UNSET)

        salvage_value = d.pop("salvageValue", UNSET)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        size = d.pop("size", UNSET)

        size_unit = d.pop("sizeUnit", UNSET)

        start_id = d.pop("startID", UNSET)

        start_value = d.pop("startValue", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AssetMasterModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AssetMasterModelStatus.from_dict(_status)

        _status_date = d.pop("statusDate", UNSET)
        status_date: Union[Unset, datetime.datetime]
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AssetMasterModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AssetMasterModelType.from_dict(_type)

        asset_master_model = cls(
            asset_id=asset_id,
            class_type=class_type,
            comments=comments,
            current_value=current_value,
            date_of_service=date_of_service,
            dependent_flag=dependent_flag,
            depreciation_amount=depreciation_amount,
            depreciation_end_date=depreciation_end_date,
            depreciation_start_date=depreciation_start_date,
            depreciation_value=depreciation_value,
            description=description,
            end_id=end_id,
            gis_objects=gis_objects,
            id=id,
            name=name,
            number=number,
            salvage_value=salvage_value,
            service_provider_code=service_provider_code,
            size=size,
            size_unit=size_unit,
            start_id=start_id,
            start_value=start_value,
            status=status,
            status_date=status_date,
            type=type,
        )

        asset_master_model.additional_properties = d
        return asset_master_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
