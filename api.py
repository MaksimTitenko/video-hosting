from fastapi import *
from typing import List
import shutil

from starlette.responses import JSONResponse

from schemas import UploadVideo, GetVideo, User, Message

video_router = APIRouter()


@video_router.post('/')
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, description=description)
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename, 'info': info}


@video_router.post('/img')
async def upload_image(files: List[UploadFile] = File(...)):
    for file in files:
        with open(file.filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {"file_name": "good"}


@video_router.get('/video', response_model=GetVideo, responses={404:{'model': Message}})
async def get_video():
    user = {'id': 25, 'name': 'Pipec'}
    video = {'title': 'Test', 'description': 'Description'}
    info = GetVideo(user=user, video=video)
    return JSONResponse(status_code=200, content=info.dict())

@video_router.get('/test')
async def get_test(req: Request):
    return {}