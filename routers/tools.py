from typing import Optional

from fastapi import APIRouter, Request

from tools.epoch_to_utc import epoch_to_utc
from tools.password_generator import generate_password

router = APIRouter()

@router.get("/tools/", tags=["tools"])
def tools_index():
    return {
        "description": "This API contains some tools for sre tasks"
    }

@router.get("/tools/password-generator", tags=["tools"])
def tools_password_generator():
    return generate_password()

@router.get("/tools/epoch-to-utc/{epoch_time}", tags=["tools"])
def tools_epoch_to_utc(epoch_time: Optional[int] = None):
    if epoch_time:
        return epoch_to_utc(epoch_time)
    return "convert epoch time to utc"
