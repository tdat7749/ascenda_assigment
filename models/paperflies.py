from data_class.common import Amenities, Hotel, Location, Images, Image
from models.base import Base
from common_functions.common import convert_to_lowercase_with_spaces

class Paperflies(Base):

  @staticmethod
  def endpoint() -> str:
    return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

  @staticmethod
  def filter_images(images: dict) -> Images:
    result = Images()

    if "rooms" in images and images["rooms"] is not None:
      result.room = [
        Image(link=item["link"], description=item["caption"])
        for item in images["rooms"]
      ]

    if "site" in images and images["site"] is not None:
      result.sites = [
        Image(link=item["link"], description=item["caption"])
        for item in images["site"]
      ]

    if "amenities" in images and images["amenities"] is not None:
      result.amenities = [
        Image(link=item["link"], description=item["caption"])
        for item in images["amenities"]
      ]

    return result
  
  @staticmethod
  def parse(obj: dict) -> Hotel:
    # get images
    if "images" in obj:
      images = Paperflies.filter_images(obj["images"])
    else:
      images = Images()

    # get amenities and convert to lowercase with space
    if "amenities" in obj and obj["amenities"] is not None:
      if "general" in obj["amenities"] and obj["amenities"]["general"] is not None:
        general = [convert_to_lowercase_with_spaces(item) for item in obj["amenities"]["general"]]
      else:
        general = []

      if "room" in obj["amenities"] and obj["amenities"]["room"] is not None:
        room = [convert_to_lowercase_with_spaces(item) for item in obj["amenities"]["room"]]
      else:
        room = []
    else:
      room = []
      general = []
      
    return Hotel(
      id=obj["hotel_id"],
      destination_id=obj["destination_id"],
      name=obj["hotel_name"],
      description=obj["details"],
      location=Location(
        address=obj["location"]["address"],
        country=obj["location"]["country"]
      ),
      images= images,
      amenities=Amenities(
        room=room,
        general=general
      ),
      booking_conditions=obj["booking_conditions"]
    )