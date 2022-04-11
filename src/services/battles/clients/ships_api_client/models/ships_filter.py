from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipsFilter")


@attr.s(auto_attribs=True)
class ShipsFilter:
    """
    Attributes:
        classes (Union[Unset, List[str]]):
        names (Union[Unset, List[str]]):
    """

    classes: Union[Unset, List[str]] = UNSET
    names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classes is not UNSET:
            field_dict["classes"] = classes
        if names is not UNSET:
            field_dict["names"] = names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classes = cast(List[str], d.pop("classes", UNSET))

        names = cast(List[str], d.pop("names", UNSET))

        ships_filter = cls(
            classes=classes,
            names=names,
        )

        ships_filter.additional_properties = d
        return ships_filter

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
