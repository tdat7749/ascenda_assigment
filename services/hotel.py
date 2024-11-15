from typing import List
from data_class.common import Hotel, Image

class HotelService:
  def __init__(self):
    pass
      
  @staticmethod
  # This function base on the "image.link" field to check and remove duplicates.
  def __unique_images(images:List[Image]) -> List[Image]:
    seen = set()
    unique = []
    for image in images:
        if image.link not in seen:
            unique.append(image)
            seen.add(image.link)
    return unique

  #
  def merge_and_save(self,hotels: List[Hotel]) -> List[Hotel]:
    merged_hotels = {}

    for hotel in hotels:
      hotel_id = hotel.id

      if hotel_id not in merged_hotels:
        merged_hotels[hotel_id] = Hotel(
          id= hotel.id,
          destination_id= hotel.destination_id,
          description= hotel.description,
          name= hotel.name,
          location= hotel.location,
          amenities= hotel.amenities,
          images= hotel.images,
          booking_conditions= hotel.booking_conditions
        )
        
      else:
        exist_hotel: Hotel =  merged_hotels[hotel_id]

        # --Merge the general info
        exist_hotel.name = max(exist_hotel.name, hotel.name, key=lambda x: len(x) if x else 0)
        exist_hotel.description = max(exist_hotel.description, hotel.description, key=lambda x: len(x) if x else 0)
        
        # --Merge the location
        exist_hotel.location.lng = hotel.location.lng if hotel.location.lng is not None else exist_hotel.location.lng
        exist_hotel.location.lat = hotel.location.lat if hotel.location.lat is not None else exist_hotel.location.lat

        exist_hotel.location.address = max(exist_hotel.location.address, hotel.location.address, key=lambda x: len(x) if x else 0)
        exist_hotel.location.country = max(exist_hotel.location.country, hotel.location.country, key=lambda x: len(x) if x else 0)
        exist_hotel.location.city = max(exist_hotel.location.city, hotel.location.city, key=lambda x: len(x) if x else 0)
      
        # --Merge the amenities
        # The data is an array of strings, so the "set" can be used to remove duplicates.
        exist_hotel.amenities.general = list(set(exist_hotel.amenities.general + hotel.amenities.general))
        exist_hotel.amenities.room = list(set(exist_hotel.amenities.room + hotel.amenities.room))

        # --Merge the images
        # The data is an array of objects, so the "set" cannot be used to remove duplicates. And the __unique_images function will do it.
        exist_hotel.images.room = HotelService.__unique_images(exist_hotel.images.room + hotel.images.room)
        
        exist_hotel.images.sites = HotelService.__unique_images(exist_hotel.images.sites + hotel.images.sites)
        
        exist_hotel.images.amenities = HotelService.__unique_images(exist_hotel.images.amenities + hotel.images.amenities)

        # --Merge the booking conditions
        exist_hotel.booking_conditions = list(set(exist_hotel.booking_conditions + hotel.booking_conditions))
        
    return list(merged_hotels.values())

  
  def find(self,hotels: List[Hotel],hotel_ids: List[str], destination_ids: List[str]) -> List[Hotel]:
    # If one of the two lists is None, it will return all the hotels
    if len(hotel_ids) == 0 or len(destination_ids) == 0:
      return hotels
      
    # If both the lists is not None, it will return only the hotels that match the criteria
    filtered_hotels = []
    for hotel in hotels:
      if hotel.id in hotel_ids and str(hotel.destination_id) in destination_ids:
        filtered_hotels.append(hotel)
        
    return filtered_hotels