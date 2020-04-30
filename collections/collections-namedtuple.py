from collections import namedtuple

RGBAColor = namedtuple("RGBAColor", ["R", "G", "B", "A"])

red = RGBAColor(R=255, G=0, B=0, A=1.0)
blue = RGBAColor(0, 0, 255, 1.0)

print(red)  # RGBAColor(R=255, G=0, B=0, A=1.0)
print(blue)  # RGBAColor(R=0, G=0, B=255, A=1.0)
print(red[0])  # 255
print(red.A)  # 1.0
print(red._asdict())  # {'R': 255, 'G': 0, 'B': 0, 'A': 1.0}


# * A namedtuple is a type which creates a class
print(type(RGBAColor))  # <class 'type'>
print(type(red))  # <class '__main__.RGBAColor'>

RGBColor = namedtuple(
    "RGB", RGBAColor._fields[:3], defaults=[0, 0]
)  # * Create a namedtuple from the fields of another
print(RGBColor._fields)  # ('R', 'G', 'B')
print(
    RGBColor._field_defaults
)  # {'G': 0, 'B': 0} # * Note that this backpopulates from the last field to the first

# ! Since namedtuple is a class it can be easily be extended using class syntax
class ExtendedRGBA(namedtuple("ExtendedRGBA", RGBColor._fields + ("A",))):
    def __new__(
        cls, R, G, B, A
    ):  # ! Override new not __init__ because tuples are immutable
        if (
            R > 255
            or B > 255
            or G > 255
            or A > 1.0
            or R < 0
            or B < 0
            or G < 0
            or A < 0.0
        ):
            raise ValueError("RGB must be [0,255] and A must be [0,1.0]")
        self = super().__new__(cls, R, G, B, A)
        return self

    def convert_to_hex(self):
        return f"#{hex(self.R).zfill(4)}{hex(self.G).zfill(4)}{ hex(self.B).zfill(4)}".replace(
            "0x", ""
        )

    def __repr__(self):
        return super(ExtendedRGBA, self).__repr__()[:-1] + f" A={self.A})"


some_color = ExtendedRGBA(123, 234, 4, 1.0)
print(some_color)  # ExtendedRGBA(R=123, G=234, B=4 A=1.0)
print(some_color.convert_to_hex())  # #7bea04

# * Alternative syntax with type hinting support; however, dynamic class creation is lost
from typing import NamedTuple


class RGBColor2(NamedTuple):
    R: int
    G: int
    B: int


class RGBAColor2(RGBColor2):
    A: float


some_color3 = RGBColor2(255, 255, 128)
print(some_color3)  # RGBColor2(R=255, G=255, B=128)
some_color3.z = 0
