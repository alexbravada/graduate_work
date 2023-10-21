import uuid

from sqlalchemy.orm import Session

from models.models import TransactionOrder


async def set_order(db: Session, **kwargs):
    db_order = TransactionOrder(**kwargs)
    await db.add(db_order)
    await db.flush()
    return db_order


async def update_order(db: Session, order_id: uuid.UUID, topup_id: uuid.UUID = None, refund_id: uuid.UUID = None):
    db_order = await db.query(TransactionOrder).filter(TransactionOrder.uuid == order_id).update(
        {'topup_transaction': topup_id, 'refund_transaction': refund_id}
    )
    await db.flush()
    return db_order

