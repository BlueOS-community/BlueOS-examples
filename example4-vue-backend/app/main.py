#! /usr/bin/env python3
from pathlib import Path

import appdirs
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi_versioning import VersionedFastAPI, version
from loguru import logger
from typing import Any


from pydantic import BaseModel


class TextData(BaseModel):
    data: str


SERVICE_NAME = "ExampleExtension4"
# logger.add(get_new_log_path(SERVICE_NAME))

app = FastAPI(
    title="Example Extension 4 API",
    description="API for an example extension that saves/loads data as files.",
)

# We always use the same file, for simplicity
user_config_dir = Path(appdirs.user_config_dir())
text_file = user_config_dir / "file.txt"

logger.info(f"Starting {SERVICE_NAME}!")
logger.info(f"Text file in use: {text_file}")

@app.post("/save", status_code=status.HTTP_200_OK)
@version(1, 0)
async def save_data(data: TextData) -> Any:
    with open(text_file, "w") as f:
        f.write(data.data)

@app.get("/load", status_code=status.HTTP_200_OK)
@version(1, 0)
async def load_data() -> Any:
    data = ""
    if text_file.exists():
        with open(text_file, "r") as f:
            data = f.read()
    return data

app = VersionedFastAPI(app, version="1.0.0", prefix_format="/v{major}.{minor}", enable_latest=True)

app.mount("/", StaticFiles(directory="static",html = True), name="static")

@app.get("/", response_class=FileResponse)
async def root() -> Any:
        return "index.html"

if __name__ == "__main__":
    # Running uvicorn with log disabled so loguru can handle it
    uvicorn.run(app, host="0.0.0.0", port=9100, log_config=None)
