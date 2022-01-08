from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')
class LineItem:
  def __init__(self, product, quantity, price):
    self.product = product
    self.quantity = quantity
    self.price = price
  def total(self):
    return self.price * self.quantity
class Order: # the Context
  def __init__(self, customer, cart, promotion=None):
    self.customer = customer
    self.cart = list(cart)
    self.promotion = promotion
  def total(self):
    if not hasattr(self, '__total'):
    self.__total = sum(item.total() for item in self.cart)
    return self.__total
  def due(self):
    if self.promotion is None:
      discount = 0
    else:
      discount = self.promotion.discount(self)
      return self.total() - discount
  def __repr__(self):
      fmt = '<Order total: {:.2f} due: {:.2f}>'
      return fmt.format(self.total(), self.due())
      class Promotion(ABC): # A estratégia de classe abstrata
 @abstractmethod
 def discount(self, order):
 """Retorna o desconto em dolars"""
class FidelityPromo(Promotion): # Primeira estratégia concreta
  """5% desconto para clientes com mais de 1000 pontos de fidelidade"""
  def discount(self, order):
      return order.total() * .05 if order.customer.fidelity >= 1000 else 0
class BulkItemPromo(Promotion): # Segunda 
   """10% de desonto para cada compra com mais de 20 itens"""
   def discount(self, order):
      discount = 0
   for item in order.cart:
      if item.quantity >= 20:
        discount += item.total() * .1
   return discount
class LargeOrderPromo(Promotion): # Tereira estratégia concreta
 """7% de desconto para lista com mais de 10 itens diferentes"""
 def discount(self, order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
      return order.total() * .07
    return 0
