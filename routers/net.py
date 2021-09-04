from fastapi import APIRouter
from libs.net_tools import whatismyip

router = APIRouter()

@router.get("/net/", tags=["net"])
async def net_index():
    return {"net_tools": "my_ip_address"}

@router.get("/net/whatismyip", tags=["net"])
async def net_whatismyip():
    return {"my_ip_address": whatismyip()}
