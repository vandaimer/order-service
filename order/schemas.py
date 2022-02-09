from pydantic import BaseModel


class OrderSchema(BaseModel):
    user_id: str
    product_code: str


class OrderInSchema(OrderSchema):
    pass


class OrderOutSchema(OrderSchema):
    id: int
