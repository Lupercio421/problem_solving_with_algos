# Write your solution here.
# Python version 3.12.3
## All the packages you need to complete this problem are already installed
## for you in our local (sandbox) virtual environment.
## Debug with sys.stderr.write

from collections.abc import Callable
from enum import Enum, auto
from typing import TypeAlias

Price: TypeAlias = float
Dollars: TypeAlias = float
TimeStamp: TypeAlias = float

class Signal(Enum):
    LONG = auto()
    HOLD = auto()
    SHORT = auto()

Strategy: TypeAlias = Callable[[Price], tuple[Signal, int]]

class Violation(Enum):
    DrawdownHit = auto()
    QuantityViolation = auto()
    QuantityViolationResolved = auto()
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class BacktestEngine():
    def __init__(self, startingCash: Dollars, strategy: Strategy) -> None:
        self.startingCash: Dollars = startingCash
        self.strategy: Strategy = strategy

    #Implement this
    def backtest(self, priceStream: list[tuple[Price, TimeStamp]]) -> list[list[tuple[TimeStamp, Violation]] | Dollars]:
        maxCashDrawdown: Dollars = self.startingCash * 0.8
        maxOrderSize: int = 200
        cash: Dollars = self.startingCash
        positionSize: int = 0
        violationHistory: list[tuple[TimeStamp, Violation]] = []

        price: Price
        time: TimeStamp

        for price, time in priceStream:
            assetValue: Dollars = round(cash + positionSize * price, 2)
            if assetValue < maxCashDrawdown:
                violationHistory.append((time, Violation.DrawdownHit))
                return [violationHistory, assetValue]
            
            currentSignal: Signal
            orderQuantity: int
            currentSignal, orderQuantity = self.strategy(price)

            if currentSignal != Signal.HOLD:
                side: int = 1 if currentSignal == Signal.LONG else -1
                newPosition: int = positionSize + side * orderQuantity
                prevOverLimit: bool = abs(positionSize) > maxOrderSize
                curOverLimit: bool = abs(newPosition) > maxOrderSize

                if not prevOverLimit or abs(newPosition) <= abs(positionSize):
                    if prevOverLimit and not curOverLimit:
                        violationHistory.append((time, Violation.QuantityViolationResolved))
                    elif not prevOverLimit and curOverLimit:
                        violationHistory.append((time, Violation.QuantityViolation))
                    cash -= side * orderQuantity * price
                    cash = round(cash, 2)
                    positionSize = newPosition
        
        return [violationHistory, assetValue]