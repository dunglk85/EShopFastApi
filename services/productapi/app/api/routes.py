from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def get_products():
    return {"message": "List of products"}

@router.post("/products")
async def create_product(product: dict):
    return {"message": "Product created", "product": product}

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"message": "Product details", "product_id": product_id}

@router.put("/products/{product_id}")
async def update_product(product_id: int, product: dict):
    return {"message": "Product updated", "product_id": product_id, "product": product}

@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return {"message": "Product deleted", "product_id": product_id}