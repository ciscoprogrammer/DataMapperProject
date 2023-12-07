from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import csv
import io
from database import get_db_connection, init_db

app = FastAPI()
templates = Jinja2Templates(directory="templates")
  

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-csv/")
async def handle_csv(file: UploadFile = File(...)):
    conn = get_db_connection()
    # Decoding with 'utf-8-sig' to handle UTF-8 with BOM. 
    # If there's no BOM, it will work as usual for UTF-8.
    data = await file.read()
    reader = csv.reader(io.StringIO(data.decode('utf-8-sig')))

    # Assuming first row is the header
    headers = next(reader)
    # Using strip to remove any whitespace that might be around the column names
    headers = [h.strip() for h in headers]
    try:
        name_index = headers.index("Name")
        age_index = headers.index("Age")
    except ValueError as e:
        conn.close()
        return {"error": str(e)}

    with conn:
        for row in reader:
            # Strip whitespace from entries as well
            name = row[name_index].strip()
            age = row[age_index].strip()
            conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.close()
    return {"message": "File processed successfully"}
