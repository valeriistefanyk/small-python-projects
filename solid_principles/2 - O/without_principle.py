class Order:
    """
        Если нужно добавить новый способ доставки,
        то придется делать весь класс Order
    """

    def __init__(self, lineitems, shippingType):
        self.lineitems = lineitems
        self.shippingType = shippingType

    def get_total(self):
        pass

    def get_total_weight(self):
        pass

    def set_shipping_type(self, shipping):
        pass

    def get_shipping_cost(self):

        if self.shippingType == 'ground':
            # Бесплатно для больших заказов
            if self.get_total > 100:
                return 0
            # $1.5 за килограмм, но не меньше $10
            return max(10, self.get_total_weight() * 1.5)

        if self.shippingType == 'air':
            # $3 за кг но не меньше $20
            return max(20, self.get_total_weight() * 3)

    def get_shipping_date(self):
        pass