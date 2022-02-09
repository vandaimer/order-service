from fastapi import APIRouter, HTTPException

from order.schemas import OrderInSchema, OrderOutSchema
from order.views import Order as OrderView
from order.log import logger


router = APIRouter()


@router.post("/order",
             response_model=OrderOutSchema,
             status_code=201,
             name="Create new Order")
async def new_order(order: OrderInSchema):
    """
    Create a new Order
    """
    try:

        new_order = await OrderView.create(order)
    except Exception:
        message = 'Error to create new Order.'
        logger.warning(f'{message} - {str(order)}')
        raise HTTPException(
            status_code=400,
            detail=message,
        )

    return new_order
