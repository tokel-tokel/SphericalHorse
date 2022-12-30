
class CircleAttrs:
    attrs = {"fill": "", "outline": ""}

    def set_color(self, color: str):
        self.attrs["fill"] = color
        self.attrs["outline"] = color

    
    def get_attrs(self) -> dict:
        return self.attrs

class RingAttrs:
    attrs = {"style": "arc", "outline": "", "width": 0}

    def __init__(self, width: int):
        self.attrs["width"] = width
    
    def set_color(self, color: str):
        self.attrs["outline"] = color
    
    def get_attrs(self) -> dict:
        return self.attrs
    