from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/api/download")
async def main():
    some_file_path = "static/images/donald_duck.png"
    return FileResponse(some_file_path)


@app.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(f"media/images/{file.filename}", "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}
