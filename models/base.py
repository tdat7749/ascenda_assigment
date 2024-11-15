from data_class.common import Hotel, Images
import requests


class Base:
  
  @staticmethod
  def endpoint() -> str:
      raise NotImplementedError

  @staticmethod
  def parse(obj: dict) -> Hotel:
      raise NotImplementedError

  @staticmethod
  def filter_images(images: dict) -> Images:
      raise NotImplementedError
    
  def fetch(self):
    url = self.endpoint()
    response = requests.get(url)

    return [self.parse(dto) for dto in response.json()]