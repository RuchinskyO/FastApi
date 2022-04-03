from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

inventory = {
    1: {
        "name":"Milk",
        "price": 3.99,
        "brand":"Regular"
}}
@app.get("/get-item/{item_id}")
def get_item(item_id:int):
 # endpoint to get data (dictinary) by /get-item/1
 # we have only one product
 # http://127.0.0.1:8000/get-item/1 ==> {"name":"Milk","price":3.99,"brand":"Regular"}
 return inventory[item_id]

@app.get("/get-item_name/{item_id}/{name}")
def get_item(item_id:int, name: str = None):  # http://127.0.0.1:8000/get-item_name/1/test
    # {"name":"Milk","price":3.99,"brand":"Regular"}
 return inventory[item_id] # str = None or str

@app.get("/get-item_name2/{item_id}")
def get_item(item_id:int = Path(None,description="The ID of the item")):  # http://127.0.0.1:8000/get-item_name/1
    # {"name":"Milk","price":3.99,"brand":"Regular"}
 return inventory[item_id] # description for http://127.0.0.1:8000/docs

# query parameter (str = None to make param optinal, else requar)
@app.get("/get-item_name")
def get_item(name: str = None):  # name: Optional[str] = None  ==> (more common)
 for item in inventory:
     if inventory[item]["name"] == name:
         return inventory[item]
     return {"Data":"Not found"}
# http://127.0.0.1:8000/get-item_name?name=Milk ==> {"name":"Milk","price":3.99,"brand":"Regular"}
# Else {"Data":"Not found"}

@app.get("/get-item_name2")
def get_item(*,name: Optional[str] = None, test: int): # *,  ==> to give params in any order
 for item in inventory:
     if inventory[item]["name"] == name:
         return inventory[item]
     return {"Data":"Not found"}

# http://127.0.0.1:8000/get-item_name2?name=Milk&test=21 ==> {"name":"Milk","price":3.99,"brand":"Regular"}

@app.get("/get-item_name3/{item_id}")
def get_item(*,item_id: int ,name: Optional[str] = None, test: int): # *,  ==> to give params in any order
 for item in inventory:
     if inventory[item]["name"] == name:
         return inventory[item]
     return {"Data":"Not found"}
# http://127.0.0.1:8000/get-item_name3/1?name=Milk&test=21 ==> OK




