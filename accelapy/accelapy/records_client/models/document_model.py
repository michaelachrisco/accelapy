import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_model_category import DocumentModelCategory
    from ..models.document_model_group import DocumentModelGroup
    from ..models.document_model_status import DocumentModelStatus
    from ..models.user_role_privilege_model import UserRolePrivilegeModel


T = TypeVar("T", bound="DocumentModel")


@_attrs_define
class DocumentModel:
    """
    Attributes:
        category (Union[Unset, DocumentModelCategory]): The document category. The list of category options varies
            depending on the document group.
        deletable (Union[Unset, UserRolePrivilegeModel]):
        department (Union[Unset, str]): The name of the department the document belongs to.
        description (Union[Unset, str]): The document description.
        downloadable (Union[Unset, UserRolePrivilegeModel]):
        entity_id (Union[Unset, str]): The unique ID of the entity or record.
        entity_type (Union[Unset, str]): The type of entity.
        file_name (Union[Unset, str]): The name of the file as it displays in the source location.
        group (Union[Unset, DocumentModelGroup]): The document group.
        id (Union[Unset, int]): The document id.
        modified_by (Union[Unset, str]): The user account that last modified the document.
        modified_date (Union[Unset, datetime.datetime]): The date the document was last modified.
        service_provider_code (Union[Unset, str]): The unique agency identifier.
        size (Union[Unset, float]): The file size of the document.
        source (Union[Unset, str]): The name for your agency's electronic document management system.
        status (Union[Unset, DocumentModelStatus]): The documet status.
        status_date (Union[Unset, datetime.datetime]): The date when the current status changed.
        title_viewable (Union[Unset, UserRolePrivilegeModel]):
        type (Union[Unset, str]): The document type.
        uploaded_by (Union[Unset, str]): The user who uploaded the document to the record.
        uploaded_date (Union[Unset, datetime.datetime]): The date when the document was uploaded.
        virtual_folders (Union[Unset, str]): This is the virtual folder for storing the attachment. With virtual folders
            you can organize uploaded attachments in groups
    """

    category: Union[Unset, "DocumentModelCategory"] = UNSET
    deletable: Union[Unset, "UserRolePrivilegeModel"] = UNSET
    department: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    downloadable: Union[Unset, "UserRolePrivilegeModel"] = UNSET
    entity_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    group: Union[Unset, "DocumentModelGroup"] = UNSET
    id: Union[Unset, int] = UNSET
    modified_by: Union[Unset, str] = UNSET
    modified_date: Union[Unset, datetime.datetime] = UNSET
    service_provider_code: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    source: Union[Unset, str] = UNSET
    status: Union[Unset, "DocumentModelStatus"] = UNSET
    status_date: Union[Unset, datetime.datetime] = UNSET
    title_viewable: Union[Unset, "UserRolePrivilegeModel"] = UNSET
    type: Union[Unset, str] = UNSET
    uploaded_by: Union[Unset, str] = UNSET
    uploaded_date: Union[Unset, datetime.datetime] = UNSET
    virtual_folders: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        deletable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deletable, Unset):
            deletable = self.deletable.to_dict()

        department = self.department
        description = self.description
        downloadable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.downloadable, Unset):
            downloadable = self.downloadable.to_dict()

        entity_id = self.entity_id
        entity_type = self.entity_type
        file_name = self.file_name
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id
        modified_by = self.modified_by
        modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        service_provider_code = self.service_provider_code
        size = self.size
        source = self.source
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        status_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        title_viewable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title_viewable, Unset):
            title_viewable = self.title_viewable.to_dict()

        type = self.type
        uploaded_by = self.uploaded_by
        uploaded_date: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_date, Unset):
            uploaded_date = self.uploaded_date.isoformat()

        virtual_folders = self.virtual_folders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if department is not UNSET:
            field_dict["department"] = department
        if description is not UNSET:
            field_dict["description"] = description
        if downloadable is not UNSET:
            field_dict["downloadable"] = downloadable
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if service_provider_code is not UNSET:
            field_dict["serviceProviderCode"] = service_provider_code
        if size is not UNSET:
            field_dict["size"] = size
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if status_date is not UNSET:
            field_dict["statusDate"] = status_date
        if title_viewable is not UNSET:
            field_dict["titleViewable"] = title_viewable
        if type is not UNSET:
            field_dict["type"] = type
        if uploaded_by is not UNSET:
            field_dict["uploadedBy"] = uploaded_by
        if uploaded_date is not UNSET:
            field_dict["uploadedDate"] = uploaded_date
        if virtual_folders is not UNSET:
            field_dict["virtualFolders"] = virtual_folders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_model_category import DocumentModelCategory
        from ..models.document_model_group import DocumentModelGroup
        from ..models.document_model_status import DocumentModelStatus
        from ..models.user_role_privilege_model import UserRolePrivilegeModel

        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[Unset, DocumentModelCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = DocumentModelCategory.from_dict(_category)

        _deletable = d.pop("deletable", UNSET)
        deletable: Union[Unset, UserRolePrivilegeModel]
        if isinstance(_deletable, Unset):
            deletable = UNSET
        else:
            deletable = UserRolePrivilegeModel.from_dict(_deletable)

        department = d.pop("department", UNSET)

        description = d.pop("description", UNSET)

        _downloadable = d.pop("downloadable", UNSET)
        downloadable: Union[Unset, UserRolePrivilegeModel]
        if isinstance(_downloadable, Unset):
            downloadable = UNSET
        else:
            downloadable = UserRolePrivilegeModel.from_dict(_downloadable)

        entity_id = d.pop("entityId", UNSET)

        entity_type = d.pop("entityType", UNSET)

        file_name = d.pop("fileName", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, DocumentModelGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = DocumentModelGroup.from_dict(_group)

        id = d.pop("id", UNSET)

        modified_by = d.pop("modifiedBy", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, datetime.datetime]
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        service_provider_code = d.pop("serviceProviderCode", UNSET)

        size = d.pop("size", UNSET)

        source = d.pop("source", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DocumentModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DocumentModelStatus.from_dict(_status)

        _status_date = d.pop("statusDate", UNSET)
        status_date: Union[Unset, datetime.datetime]
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        _title_viewable = d.pop("titleViewable", UNSET)
        title_viewable: Union[Unset, UserRolePrivilegeModel]
        if isinstance(_title_viewable, Unset):
            title_viewable = UNSET
        else:
            title_viewable = UserRolePrivilegeModel.from_dict(_title_viewable)

        type = d.pop("type", UNSET)

        uploaded_by = d.pop("uploadedBy", UNSET)

        _uploaded_date = d.pop("uploadedDate", UNSET)
        uploaded_date: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_date, Unset):
            uploaded_date = UNSET
        else:
            uploaded_date = isoparse(_uploaded_date)

        virtual_folders = d.pop("virtualFolders", UNSET)

        document_model = cls(
            category=category,
            deletable=deletable,
            department=department,
            description=description,
            downloadable=downloadable,
            entity_id=entity_id,
            entity_type=entity_type,
            file_name=file_name,
            group=group,
            id=id,
            modified_by=modified_by,
            modified_date=modified_date,
            service_provider_code=service_provider_code,
            size=size,
            source=source,
            status=status,
            status_date=status_date,
            title_viewable=title_viewable,
            type=type,
            uploaded_by=uploaded_by,
            uploaded_date=uploaded_date,
            virtual_folders=virtual_folders,
        )

        document_model.additional_properties = d
        return document_model

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
