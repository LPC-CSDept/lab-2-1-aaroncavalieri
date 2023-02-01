def main():
   ##################################################
   original_price = int(input("Orginial Price: "))
   rate = int(input("Discount Amount: "))
   discount_amount = (original_price * (rate / 100))
   final_price = original_price - discount_amount
   print ("Regular Price: " + "$" + str(original_price))
   print ("Discount Amount: " + "$" + str(discount_amount))
   print ("The Final Price: " + "$" + str(final_price))
   ##################################################

pass


if __name__ == '__main__':
    main()
