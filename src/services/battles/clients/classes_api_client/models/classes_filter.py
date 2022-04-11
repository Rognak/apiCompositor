from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClassesFilter")


@attr.s(auto_attribs=True)
class ClassesFilter:
    """
    Example:
        {'countries': ['USA'], 'type': 'bb'}

    Attributes:
        classes (Union[Unset, List[str]]):
        countries (Union[Unset, List[str]]):
        type (Union[Unset, str]):
    """

    classes: Union[Unset, List[str]] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classes is not UNSET:
            field_dict["classes"] = classes
        if countries is not UNSET:
            field_dict["countries"] = countries
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classes = cast(List[str], d.pop("classes", UNSET))

        countries = cast(List[str], d.pop("countries", UNSET))

        type = d.pop("type", UNSET)

        classes_filter = cls(
            classes=classes,
            countries=countries,
            type=type,
        )

        classes_filter.additional_properties = d
        return classes_filter

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
