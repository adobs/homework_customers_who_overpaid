def customer_payment_recorder(path):
    """
    takes an order file and returns the amount overpaid and underpaid


    """
    record_log = open(path)

    customers_underpaid = {}
    customers_overpaid = {}
    customers_paid = []

    for entry in record_log:
        entry = entry.rstrip()
        entry = entry.split("|")

        customer_name = entry[1]
        qty_melons_ordered = int(entry[2])
        price_paid = float(entry[3])
        price_of_melon = 1.00


        #define customers who overpaid, and underpaid
        if qty_melons_ordered*price_of_melon < price_paid:
            customers_overpaid[customer_name] = price_paid - price_of_melon*qty_melons_ordered  
        elif qty_melons_ordered*price_of_melon > price_paid:
            customers_underpaid[customer_name] = price_of_melon*qty_melons_ordered -price_paid 
        else:
            customers_paid.append(customer_name)

        #calculate amount overpaid, and undepaid
        overpaid_amount = sum(customers_overpaid.itervalues())
        underpaid_amount = sum(customers_underpaid.itervalues())

        #calculated number of customers who overpaid, and underpaid
        number_of_customers_underpay = len(customers_underpaid)
        number_of_customers_overpay = len(customers_overpaid)
        number_of_customers_correct = len(customers_paid)

    print "CUSTOMERS OVERPAID"
    print "{} customers underpaid by ${:+.2f}".format(number_of_customers_underpay,underpaid_amount)
    print
    print "CUSTOMERS UNDERPAID"
    print "{} customers overpay by ${:+.2f}".format(number_of_customers_overpay, overpaid_amount)
    print
    print "CUSTOMERS PAID CORRECTLY"
    print "{} customers correctly paid".format(number_of_customers_correct)
    



customer_payment_recorder("customer-orders.txt")





