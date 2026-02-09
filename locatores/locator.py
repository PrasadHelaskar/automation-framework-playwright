from dataclasses import dataclass
from typing import Optional

from locatores.strategies import LocateBy

@dataclass(frozen=True)
class Locator:

    by: LocateBy
    value: str
    name: Optional[str] = None
    index: Optional[int] = None


    def resolve(self, page):

        match self.by:
            case LocateBy.ROLE:
                if self.name:
                    element = page.get_by_role(self.value, name=self.name)
                else:
                    raise ValueError(f"locate strategy: {self.by} but missing name paramater")
                
            case LocateBy.TEST_ID:
                element = page.get_by_test_id(self.value)

            case LocateBy.TEXT:
                element = page.get_by_text(self.value)

            case LocateBy.LABEL:
                element = page.get_by_label(self.value)

            case LocateBy.PLACEHOLDER:
                element = page.get_by_placeholder(self.value)

            case LocateBy.CSS:
                element = page.locator(self.value)

            case LocateBy.XPATH:
                element = page.locator(f"xpath={self.value}")

            case _:
                raise ValueError(f"Unsupported locate strategy: {self.by}")

        return element.nth(self.index) if self.index is not None else element
