from fastapi import FastAPI

# pip install fastapi,pip install uvicorn

app = FastAPI()

# endpoints: /, /hello, /get-item, /about
# method POST - (Create),GET - (Read), PUT - (Update/Replace),PATCH - (Update/Modify), DELETE - (Delete)

@app.get("/")
def home():
    return {"Data":"Testing"}

# to run CMD run==> uvicorn Lesson01:app --reload      ==> http://127.0.0.1:8000
# to enter FAST-API UI ==> http://127.0.0.1:8000/docs

@app.get("/about")
def about():
    return {"Data":"About"}