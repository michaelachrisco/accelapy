from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_type_model_group import DocumentTypeModelGroup


T = TypeVar("T", bound="DocumentTypeModel")


@_attrs_define
class DocumentTypeModel:
    """
    Attributes:
        deletable (Union[Unset, bool]): Indicates whether or not the record can be deleted.
        downloadable (Union[Unset, bool]): Indicates whether or not the document type can be downloaded.
        group (Union[Unset, DocumentTypeModelGroup]): The document group for the document category.
        id (Union[Unset, str]): The document category system id assigned by the Civic Platform server.
        text (Union[Unset, str]): The localized display text.
        uploadable (Union[Unset, bool]): Indicates whether or not you can upload documents of the specified category.
        value (Union[Unset, str]): The document category value.
        viewable (Union[Unset, bool]): Indicates whether or not you can view the document category associated with the
            record.
    """

    deletable: Union[Unset, bool] = UNSET
    downloadable: Union[Unset, bool] = UNSET
    group: Union[Unset, "DocumentTypeModelGroup"] = UNSET
    id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    uploadable: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    viewable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deletable = self.deletable
        downloadable = self.downloadable
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id
        text = self.text
        uploadable = self.uploadable
        value = self.value
        viewable = self.viewable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if downloadable is not UNSET:
            field_dict["downloadable"] = downloadable
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if uploadable is not UNSET:
            field_dict["uploadable"] = uploadable
        if value is not UNSET:
            field_dict["value"] = value
        if viewable is not UNSET:
            field_dict["viewable"] = viewable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_type_model_group import DocumentTypeModelGroup

        d = src_dict.copy()
        deletable = d.pop("deletable", UNSET)

        downloadable = d.pop("downloadable", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, DocumentTypeModelGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = DocumentTypeModelGroup.from_dict(_group)

        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        uploadable = d.pop("uploadable", UNSET)

        value = d.pop("value", UNSET)

        viewable = d.pop("viewable", UNSET)

        document_type_model = cls(
            deletable=deletable,
            downloadable=downloadable,
            group=group,
            id=id,
            text=text,
            uploadable=uploadable,
            value=value,
            viewable=viewable,
        )

        document_type_model.additional_properties = d
        return document_type_model

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
