from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File, Unset

T = TypeVar("T", bound="V4PostRecordsRecordIdDocumentsMultipartData")


@_attrs_define
class V4PostRecordsRecordIdDocumentsMultipartData:
    """
    Attributes:
        uploaded_file (File): Specify the filename parameter with the file to be uploaded. See example for details.
        file_info (str): A string array containing the file metadata for each specified filename. See example for
            details.
    """

    uploaded_file: File
    file_info: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uploaded_file = self.uploaded_file.to_tuple()

        file_info = self.file_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadedFile": uploaded_file,
                "fileInfo": file_info,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uploaded_file = self.uploaded_file.to_tuple()

        file_info = (
            self.file_info if isinstance(self.file_info, Unset) else (None, str(self.file_info).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "uploadedFile": uploaded_file,
                "fileInfo": file_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uploaded_file = File(payload=BytesIO(d.pop("uploadedFile")))

        file_info = d.pop("fileInfo")

        v4_post_records_record_id_documents_multipart_data = cls(
            uploaded_file=uploaded_file,
            file_info=file_info,
        )

        v4_post_records_record_id_documents_multipart_data.additional_properties = d
        return v4_post_records_record_id_documents_multipart_data

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
