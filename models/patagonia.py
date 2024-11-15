from data_class.common import Amenities, Hotel, Image, Images, Location
from models.base import Base
from common_functions.common import convert_to_lowercase_with_spaces

class Patagonia(Base):

  @staticmethod
  def endpoint() -> str:
    return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

  @staticmethod
  def filter_images(images: dict) -> Images:
    result = Images()

    if "rooms" in images and images["rooms"] is not None:
      result.room = [
        Image(link=item["url"], description=item["description"])
        for item in images["rooms"]
      ]

    if "sites" in images and images["sites"] is not None:
      result.sites = [
        Image(link=item["url"], description=item["description"])
        for item in images["sites"]
      ]

    if "amenities" in images and images["amenities"] is not None:
      result.amenities = [
        Image(link=item["url"], description=item["description"])
        for item in images["amenities"]
      ]

    return result
  
  @staticmethod
  def parse(obj: dict) -> Hotel:
    # get images
    if "images" in obj:
      images = Patagonia.filter_images(obj["images"])
    else:
      images = Images()

    # get amenities and convert to lowercase with space
    if "amenities" in obj and obj["amenities"] is not None:
      room = [convert_to_lowercase_with_spaces(item) for item in obj["amenities"]]
    else:
      room = []
      
    return Hotel(
      id=obj["id"],
      destination_id=obj["destination"],
      name=obj["name"],
      description=obj["info"],
      location=Location(
        address=obj["address"],
        lat=obj["lat"],
        lng=obj["lng"]
      ),
      images = images,
      amenities=Amenities(
        room=room
      ),
    )