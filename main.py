#*) Create suitable data structure to store the product details such as product,unit price,gst,quantity in python

products = [
    {
        "product_name": "Leather wallet",
        "unit_price": 1100,
        "gst": 0.18,
        "quantity": 1
    }, {
        "product_name": "Umbrella",
        "unit_price": 900,
        "gst": 0.12,
        "quantity": 4
    }
    , {
        "product_name": "Cigarette",
        "unit_price": 200,
        "gst": 0.28,
        "quantity": 3
    }
    , {
        "product_name": "Honey",
        "unit_price": 100,
        "gst": 0,
        "quantity": 2
    }
]



#1)Identiy the product for which we paid maximum gst amount

def cal_gst(products):
    unit_price = products["unit_price"]
    quantity = products["quantity"]
    gst = products["gst"]

    gst_amount = unit_price * gst * quantity
    return gst_amount


maximum_gst_product = None
maximum_gst_amount = 0

for product in products:
    cur_gst_amt = cal_gst(product)
    if cur_gst_amt > maximum_gst_amount:
        maximum_gst_amount = cur_gst_amt
        maximum_gst_product = product

if maximum_gst_product is not None:
    print(f"The product with the maximum GST amount is {maximum_gst_product['product_name']}")
    print(f"GST amount is ${maximum_gst_amount:.2f}")
else:
    print("None")

#2)Cal the total amount to be paid

def total_cost(products):
    unit_price = products["unit_price"]
    gst = products["gst"]
    quantity = products["quantity"]

    total_cast_paid = unit_price * (1+gst) * quantity
    return total_cast_paid

total_amount = 0
for product in products:
    total_amount += total_cost(product)

print(f"The total_amount to be paid to the shop-keeper is ${total_amount:.2f}")
