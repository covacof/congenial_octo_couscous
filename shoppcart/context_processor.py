def total_price_shoppcart(request):
    total=0
    if 'shoppcart' in request.session:
        for key, value in request.session["shoppcart"].items():
            total=total+(float(value["price"])*value["amount"])
    return {"total_price_shoppcart":total}
