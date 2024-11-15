from data_class.common import Amenities, Hotel, Location, Image, Images
from models.base import Base
from common_functions.common import convert_to_lowercase_with_spaces

class Acme(Base):

  @staticmethod
  def endpoint() -> str:
    return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
  
  @staticmethod
  def parse(obj: dict) -> Hotel:

    # get amenities and convert to lowercase with space
    if "Facilities" in obj and obj["Facilities"] is not None:
      general = [convert_to_lowercase_with_spaces(item) for item in obj["Facilities"]]
    else:
      general = []
    
    return Hotel(
      id=obj["Id"],
      destination_id=obj["DestinationId"],
      name=obj["Name"],
      description=obj["Description"],
      location=Location(
        address=obj["Address"],
        city=obj["City"],
        country=obj["Country"],
        lat=obj["Latitude"],
        lng=obj["Longitude"]
      ),
      amenities=Amenities(
        general= general
      ),
      images= Images() # In Amce the "images" field does not exist
    )