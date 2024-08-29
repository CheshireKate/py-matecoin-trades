import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    for trade in trades:
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price
        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
