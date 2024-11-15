from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Location:
  address: Optional[str] = None
  city: Optional[str] = None
  country: Optional[str] = None
  lat: Optional[float] = None
  lng: Optional[float] = None

@dataclass
class Amenities:
  general: list[str] = field(default_factory=list)
  room: list[str] = field(default_factory=list)

@dataclass
class Image:
  link: str
  description: str

@dataclass
class Images:
  room: list[Image] = field(default_factory=list)
  sites: list[Image] = field(default_factory=list)
  amenities: list[Image] = field(default_factory=list)

@dataclass
class Hotel:
  id:str
  destination_id: int
  name: str
  description: str
  location: Location
  amenities: Amenities
  images: Images
  booking_conditions: list[str] = field(default_factory=list)
  