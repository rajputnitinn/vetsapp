def compute_taxes(amount,tax):
    amount_to_pay = amount+amount*tax
    return amount_to_pay
print("compute_taxes is:",compute_taxes)
fun = compute_taxes
print("fun is:", fun)
result = fun(amount=400, tax=0.20)
print("Result is:", result)