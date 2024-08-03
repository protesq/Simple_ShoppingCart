class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.cart = {}
        self.cart_count = {}

    def add_item(self, name, price):
        self.items[name] = price

    def cartt(self, name, price):
        if name in self.cart:
            self.cart[name] += price
        else:
            self.cart[name] = price

        if name in self.cart_count:
            self.cart_count[name] += 1
        else:
            self.cart_count[name] = 1

        list_cart = list(self.cart.items())
        print("Sepetteki Ürünler: ", list_cart)
        print("Ürün Adetleri: ", self.cart_count)

        cart_price = self.cart.values()
        total = sum(cart_price)
        print("Ödenecek Tutar: {}".format(total))

    def remove_cartt(self, name):
        if name in self.cart:
            self.cart[name] -= self.items[name]
            if self.cart[name] <= 0:
                del self.cart[name]
            if name in self.cart_count:
                self.cart_count[name] -= 1
                if self.cart_count[name] == 0:
                    del self.cart_count[name]
            else:
                print(f"{name} ürününden sepetinizde yok.")
        else:
            print(f"{name} ürünü sepetinizde bulunmamaktadır.")

        list_cart = list(self.cart.items())
        print("Sepetteki Ürünler: ", list_cart)
        print("Ürün Adetleri: ", self.cart_count)

        cart_price = self.cart.values()
        total = sum(cart_price)
        print("Ödenecek Tutar: {}".format(total))

    def cart_price(self):
        cart_price = self.cart.values()
        total = sum(cart_price)
        print("Ödenecek Tutar: {}".format(total))


i = ShoppingCart()
i.add_item("Apple", 100)
i.add_item("Banana", 200)
i.add_item("Cherry", 300)
a = 0
item_list = list(i.items.items())
for name, price in i.items.items():
    a = a + 1
    print(f"{a} {name}: {price}")

while True:
    try:
        c = int(input("Sepete ekleyeceğiniz ürünün idsini yazınız. Ödemeyi hesaplamak için 9'a basın. Ürün çıkarmak için 0'a basın: "))
        if c == 9:
            cart_price = i.cart.values()
            total = sum(cart_price)
            print("Ödenecek Tutar: {}".format(total))
            break
        elif c == 0:
            remove_id = int(input("Çıkarılacak ürünün idsini yazınız: "))
            if remove_id == 1:
                i.remove_cartt("Apple")
            elif remove_id == 2:
                i.remove_cartt("Banana")
            elif remove_id == 3:
                i.remove_cartt("Cherry")
            else:
                print("Hata! Geçersiz ID.")
        elif c == 1:
            i.cartt("Apple", 100)
        elif c == 2:
            i.cartt("Banana", 200)
        elif c == 3:
            i.cartt("Cherry", 300)
        else:
            print("Hata! Geçersiz ID.")
    except Exception as e:
        print("Hata! Geçersiz giriş.")
