import random

global wallet
global start_wallet
global start_price
global start_amount
global amount
global difference
global price
global choice
global liste
global new_price
global price_before_drop


def start():
    global start_wallet
    global start_price
    global start_amount
    global price
    global wallet
    start_wallet = 1000
    start_price = 10
    start_amount = 0
    price = start_price
    wallet = start_wallet


def start_buy():
    global amount
    global wallet
    amount = wallet / price
    print(f"amount: {amount}")
    wallet = 0


start()
start_buy()


def price_check():
    zero = 0
    if new_price == zero:
        print("fiyat 0 oldu")
        update_price()

    elif new_price > zero:
        pass
    else:
        print("fiyat 0 oldu")
        update_price()


def price_update():
    limit = 100
    if choice == liste[0]:
        price_gap = new_price - price
        price_checker_1 = price_gap / price * 100
        price_checker = round(price_checker_1, 2)
        if wallet != 0 and price_checker >= 3:
            print(f"buying coins for: {new_price}")
            buy()
        print(f"son artis yuzdesi : {round(price_checker, 2)} %")
    else:
        price_gap = price_before_drop - new_price
        price_checker = price_gap / price_before_drop * 100
        price_diff = price_before_drop - new_price
        # 100 * 8 / 10
        if price_checker >= 10 and amount != 0:
            print(f"selling coins for: {new_price}, - {round(price_checker, 2)}% ")
            sell()
        elif price_checker >= limit:
            print("paran sifirlandi")
        else:
            print(f"baslangic fiyatindan dusus orani: {round(price_checker, 2)} %")


def price_not_zero():
    pass


def update_price():
    global price
    global difference
    global choice
    global liste
    global new_price
    global price_before_drop

    liste = ['arti', 'eksi']
    choice = random.choice(liste)
    difference = random.randint(1, 10)
    price_before_drop = price
    if choice == liste[0]:
        for c in range(difference):
            new_price = price + 1
            print(f"fiyat artti, yeni fiyat: {new_price}")
            price_update()
            price = new_price
    else:
        for c in range(difference):
            new_price = price - 1
            price_check()
            print(f"fiyat dustu, yeni fiyat: {new_price}")
            price_update()
            price = new_price


def buy():
    global amount
    global wallet
    amount = wallet / new_price
    print(f"amount: {amount}")
    wallet = 0


def sell():
    global wallet
    global amount
    wallet = new_price * amount
    print(f"cuzdan degeri: {round(wallet, 2)}")
    amount = 0


for i in range(100):
    print(f"wallleeeettt {wallet}")
    print(f"amouuuunt {amount}")
    print(f"islem gunu: {i}")
    update_price()
    price_check()


if amount != 0:
    sell()

print(f"wallet: {wallet}")
print(f"amount: {amount}")
