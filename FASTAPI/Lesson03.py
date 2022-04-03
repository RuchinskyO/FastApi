from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None



class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {} # Empty for entering data

@app.get("/get-item-id/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item")):
    return inventory[item_id]

# Request Body & POST Method
@app.post("/create-item/{item_id}")
def get_item(*, item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = {"name": item.name, "brand": item.brand,
                          "price": item.price}
    return inventory[item_id]
# http://127.0.0.1:8000/create-item/2 ==> {"detail":"Method Not Allowed"}
# http://127.0.0.1:8000/docs ==> enter item "2..." manually, but it will store only in memory not in code

# Better way: BUT now we need to change "get" as well .name
@app.post("/create-item2/{item_id}")
def create_item(*, item_id: int, item: Item):
    if item_id in inventory:
        #return {"Error": "Item ID already exists"}
        raise HTTPException(status_code=400, detail="Item ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.get("/get-by-name/")
def get_item(name: str = Query(None, title="Name", description="Name of item")):
 for item_id in inventory:
     if inventory[item_id].name == name:
         return inventory[item_id]
     #return {"Data":"Not found"}
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

# http://127.0.0.1:8000/docs
# With /create-item2/{item_id} entering n-number of products
# "/get-item-id/{item_id}" ==> 1,2,.. IDs getting right product
# "/get-by-name" ==> milk,eggs... by name getting right product

## UPDATE
@app.put("/update-item/{item_id}")
def update_item(*, item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists"}
    if item.name != None:
       inventory[item_id].name = item.name
    if item.price != None:
       inventory[item_id].price = item.price
    if item.brand != None:
       inventory[item_id].brand = item.brand
    return inventory[item_id]
# create /create-item2/{item_id} {"name": "Milk","price": 7} UPDATE /update-item/{item_id}  {"brand": "Cold"} ==>  {"name": "Milk","price": 7, "brand": "Cold"}

## DELETE

@app.delete("/delete-item/")
def delete_item(item_id: int = Query(..., description="The ID of item to be deleted")): # ..., to make it mandatory
    if item_id not in inventory:
        return {"Error":"ID does not exist."}
    del inventory[item_id]
    return {"Success":"Item deleted!"}

