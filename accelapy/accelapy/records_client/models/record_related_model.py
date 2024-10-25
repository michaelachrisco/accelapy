from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_related_model_relationship import RecordRelatedModelRelationship
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_type_no_alias_model import RecordTypeNoAliasModel


T = TypeVar("T", bound="RecordRelatedModel")


@_attrs_define
class RecordRelatedModel:
    """
    Attributes:
        custom_id (Union[Unset, str]): An ID based on a different numbering convention from the numbering convention
            used by the record ID (xxxxx-xx-xxxxx). Accela Automation auto-generates and applies an alternate ID value when
            you submit a new application.
        id (Union[Unset, str]): The record system id assigned by the Civic Platform server.
        relationship (Union[Unset, RecordRelatedModelRelationship]): The type of relationship of a related record.
        service_prove_code (Union[Unset, str]): The unique agency id.
        tracking_id (Union[Unset, int]): The application tracking number (IVR tracking number).
        type (Union[Unset, RecordTypeNoAliasModel]):
    """

    custom_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    relationship: Union[Unset, RecordRelatedModelRelationship] = UNSET
    service_prove_code: Union[Unset, str] = UNSET
    tracking_id: Union[Unset, int] = UNSET
    type: Union[Unset, "RecordTypeNoAliasModel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_id = self.custom_id
        id = self.id
        relationship: Union[Unset, str] = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship.value

        service_prove_code = self.service_prove_code
        tracking_id = self.tracking_id
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if id is not UNSET:
            field_dict["id"] = id
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if service_prove_code is not UNSET:
            field_dict["serviceProveCode"] = service_prove_code
        if tracking_id is not UNSET:
            field_dict["trackingId"] = tracking_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_type_no_alias_model import RecordTypeNoAliasModel

        d = src_dict.copy()
        custom_id = d.pop("customId", UNSET)

        id = d.pop("id", UNSET)

        _relationship = d.pop("relationship", UNSET)
        relationship: Union[Unset, RecordRelatedModelRelationship]
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = RecordRelatedModelRelationship(_relationship)

        service_prove_code = d.pop("serviceProveCode", UNSET)

        tracking_id = d.pop("trackingId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RecordTypeNoAliasModel]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RecordTypeNoAliasModel.from_dict(_type)

        record_related_model = cls(
            custom_id=custom_id,
            id=id,
            relationship=relationship,
            service_prove_code=service_prove_code,
            tracking_id=tracking_id,
            type=type,
        )

        record_related_model.additional_properties = d
        return record_related_model

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
