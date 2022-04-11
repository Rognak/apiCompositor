from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Classes")


@attr.s(auto_attribs=True)
class Classes:
    """
    Attributes:
        cls (str):
        type (str):
        country (str):
        num_guns (int):
        bore (float):
        displacement (int):
    """

    cls: str
    type: str
    country: str
    num_guns: int
    bore: float
    displacement: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cls = self.cls
        type = self.type
        country = self.country
        num_guns = self.num_guns
        bore = self.bore
        displacement = self.displacement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cls": cls,
                "type": type,
                "country": country,
                "num_guns": num_guns,
                "bore": bore,
                "displacement": displacement,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clss = d.pop("cls")

        type = d.pop("type")

        country = d.pop("country")

        num_guns = d.pop("num_guns")

        bore = d.pop("bore")

        displacement = d.pop("displacement")

        classes = cls(
            cls=clss,
            type=type,
            country=country,
            num_guns=num_guns,
            bore=bore,
            displacement=displacement,
        )

        classes.additional_properties = d
        return classes

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
