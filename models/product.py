from pydantic import BaseModel

class ProductResponse(BaseModel):
    productId: int
    productCode: str
    productName: str
    isActive: bool