from datetime import datetime, timedelta
import time
import uuid
import random


class OrdersManager:
    __orders = []
    __orders_processed = 0
    __last_printed_log = datetime.now()

    def __init__(self) -> None:
        self.__generate_fake_orders(quantity=1_000)

    def __generate_fake_orders(self, quantity):
        self.__log(f"Generating fake orders")
        self.__orders = [(uuid.uuid4(), x) for x in range(quantity)]
        self.__log(f"{len(self.__orders)} generated...")

    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order

        self.__log(
            message=f"Order [{id}] {number} was successfully prosecuted."
        )

        time.sleep(random.uniform(0, 1))

    def process_orders(self):
        for order in self.__orders:
            self.__fake_save_on_db(order=order)
            self.__orders_processed += 1
            if datetime.now() > self.__last_printed_log:
                self.__last_printed_log = datetime.now() + timedelta(seconds=5)
                self.__log(
                    message=f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}"
                )


#
#
# ---
orders_manager = OrdersManager()

start_time = time.time()

orders_manager.process_orders()

delay = time.time() - start_time

print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")