import zope.interface


class Order:
    
    def __init__(self, lineitems, shippingType):
        self.lineitems = lineitems
        self.shippingType = IShippingType()

    def get_total(self):
        return 2

    def get_total_weight(self):
        return 20

    def set_shipping_type(self, shipping):
        self.shippingType = shipping

    def get_shipping_cost(self):
        return self.shippingType.get_cost(self)

    def get_shipping_date(self):
        return self.shippingType.get_date(self)


class IShippingType(zope.interface.Interface):
    def get_cost(self, order):
        """ get cost """
    def get_date(self, order):
        """ get cost """


@zope.interface.implementer(IShippingType)
class Ground:

    def get_cost(self, order):
        if order.get_total > 100:
            return 0
        # $1.5 за килограмм, но не меньше $10
        return max(10, order.get_total_weight() * 1.5)
   
    def get_date(self, order):
        pass


@zope.interface.implementer(IShippingType)
class Air:

    def get_cost(self, order):
        # $3 за кг но не меньше $20
        return max(20, order.get_total_weight() * 3)

    def get_date(self, order):
        pass