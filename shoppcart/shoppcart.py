
class Shoppcart:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        shoppcart=self.session.get("shoppcart")
        if not shoppcart:
            shoppcart=self.session["shoppcart"]={}
        #else:
        self.shoppcart=shoppcart


    def add(self, product):
        if(str(product.id) not in self.shoppcart.keys()):
            self.shoppcart[product.id]={
                "product_id":product.id,
                "name":product.name,
                "price":str(product.price),
                "amount":1,
                "image":product.image.url,
            }
        else:
            for key, value in self.shoppcart.items():
                if key==str(product.id):
                    value["amount"]=value["amount"]+1
                    value["price"]=float(value["price"])+product.price
                    break

        self.save_shoppcart()


    def save_shoppcart(self):
        self.session["shoppcart"]=self.shoppcart
        self.session.modified=True



    def delete(self, product):
        product.id=str(product.id)
        if product.id in self.shoppcart:
            del self.shoppcart[product.id]
            self.save_shoppcart()


    def remove_product(self, product):
        for key, value in self.shoppcart.items():
            if key == str(product.id):
                value["amount"] = value["amount"] - 1
                value["price"] = float(value["price"]) - product.price
                if value["amount"]<1:
                    self.delete(product)
                break
        self.save_shoppcart()


    def clean_shoppcart(self):
        self.session["shoppcart"]={}
        self.session.modified=True


