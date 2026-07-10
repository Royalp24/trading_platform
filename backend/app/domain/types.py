from datetime import datetime
from decimal import Decimal
from uuid import UUID

from app.core.enums import TimeFrame as CoreTimeFrame

type PriceValue = Decimal
type Quantity = Decimal
type Percentage = Decimal
type Volume = Decimal
type Money = Decimal
type Symbol = str
type Exchange = str
type TimeFrame = CoreTimeFrame
type UUIDType = UUID
type Timestamp = datetime
