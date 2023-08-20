import httpx
from fastapi import Header, HTTPException, status


async def validate_auth_key(auth_key: str) -> bool:
    url = "/auth/v1/access"  # URL микросервиса auth
    headers = {"Authorization": auth_key}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    if response.status_code == status.HTTP_200_OK:
        return True
    else:
        return False


async def check_auth_key(auth_key: str = Header(...)):
    is_valid = await validate_auth_key(auth_key)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Invalid auth key")
    return True
