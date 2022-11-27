from fastapi import APIRouter


router = APIRouter(
    prefix="/menu",
    tags=["menu"],
    responses={404: {"description": "Not found"}},
)


fake_menu_items = [
    {'name': 'Burger'}, {'name': 'Pizza'}
]


@router.get("/")
async def read_items():
    return fake_menu_items
