import argparse
import json
from dataclasses import asdict
from data_class.common import Hotel
from models.acme import Acme
from models.paperflies import Paperflies
from models.patagonia import Patagonia
from services.hotel import HotelService
from typing import List

def fetch_hotels(hotel_ids: List[str], destinations_ids: List[str]):
  suppliers = [
    Acme(),
    Paperflies(),
    Patagonia(),
  ]
  # fetch all data
  all_supplier_data:List[Hotel] = []
  for supp in suppliers:
    all_supplier_data.extend(supp.fetch())

  svc = HotelService()
  # merge hoteles
  all_data = svc.merge_and_save(all_supplier_data)

  # filter hotel base on hotel_ids and destinations_ids
  filtered_data = svc.find(all_data, hotel_ids, destinations_ids)

  # convert data to dict
  dict_result = [asdict(hotel) for hotel in filtered_data]
  
  return json.dumps(dict_result, indent = 2)


def main():
  parser = argparse.ArgumentParser()

  parser.add_argument("hotel_ids",type=str,help="Hotel IDs")
  parser.add_argument("destination_ids",type=str,help="Destination IDs")

  args = parser.parse_args()
  
  # get args
  if not args.hotel_ids or args.hotel_ids.lower().strip() == "none":
    hotel_ids = []
  else:
    hotel_ids = args.hotel_ids.split(",")
    
  if not args.destination_ids or args.destination_ids.lower().strip() == "none":
    destination_ids = []
  else:
    destination_ids = args.destination_ids.split(",")

  
  result = fetch_hotels(hotel_ids,destination_ids)

  print(result)

if __name__ == "__main__":
  main()