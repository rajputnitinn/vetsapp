#re define function

def compute_taxes(amount=100,tax=0.18):
    amount_to_pay = amount+amount*tax
    return amount_to_pay
print("compute_taxes is",compute_taxes)

def compute_taxes(amount=100,tax=0.18,extra=0.10):
    amount_to_pay = amount+amount*tax+amount*extra
    return amount_to_pay
print("compute_taxes now is",compute_taxes)
print(compute_taxes())