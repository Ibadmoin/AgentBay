"""
Utility functions to convert between Pydantic models and SQLAlchemy models.
"""
from typing import List
from ..agent_models import Product, Bid
from ..db_models import ProductDB, BidDB
from ...enums.enums import BidStatus
from datetime import datetime

def product_db_to_pydantic(product_db: ProductDB) -> Product:
    """
    Convert SQLAlchemy ProductDB model to Pydantic Product model.
    """
    return Product(
        id=product_db.id,
        title=product_db.title,
        description=product_db.description,
        condition=product_db.condition,
        category=product_db.category,
        suggested_price=product_db.suggested_price,
        current_bid=product_db.current_bid,
        tags=product_db.tags or [],
        brand=product_db.brand,
        model=product_db.model,
        confidence_score=product_db.confidence_score,
        image_url=product_db.image_url
    )


def product_pydantic_to_db(product: Product) -> ProductDB:
    """
    Convert Pydantic Product model to SQLAlchemy ProductDB model.
    """
    return ProductDB(
        title=product.title,
        description=product.description,
        condition=product.condition,
        category=product.category,
        suggested_price=product.suggested_price,
        current_bid=product.current_bid,
        tags=product.tags,
        brand=product.brand,
        model=product.model,
        confidence_score=product.confidence_score,
        image_url=product.image_url
    )


def bid_db_to_pydantic(bid_db: BidDB) -> Bid:
    """
    Convert SQLAlchemy BidDB model to Pydantic Bid model.
    """
    return Bid(
        user_id=bid_db.user_id,
        product_id=str(bid_db.product_id),
        amount=bid_db.amount,
        timestamp=bid_db.timestamp,
        status=BidStatus(bid_db.status),
        is_auto_bid=bid_db.is_auto_bid,
        max_auto_bid=bid_db.max_auto_bid
    )


def bid_pydantic_to_db(bid: Bid, product_id: int) -> BidDB:
    """
    Convert Bid model to SQLAlchemy BidDB model.
    """
    return BidDB(
        user_id=bid.user_id,
        product_id=product_id,
        amount=bid.amount,
        timestamp=bid.timestamp,
        status=bid.status.value,
        is_auto_bid=bid.is_auto_bid,
        max_auto_bid=bid.max_auto_bid
    )