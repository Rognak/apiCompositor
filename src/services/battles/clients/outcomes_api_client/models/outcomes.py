from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Outcomes")


@attr.s(auto_attribs=True)
class Outcomes:
    """
    Attributes:
        ship (str):
        battle (str):
        result (str):
    """

    ship: str
    battle: str
    result: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship = self.ship
        battle = self.battle
        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ship": ship,
                "battle": battle,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ship = d.pop("ship")

        battle = d.pop("battle")

        result = d.pop("result")

        outcomes = cls(
            ship=ship,
            battle=battle,
            result=result,
        )

        outcomes.additional_properties = d
        return outcomes

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
