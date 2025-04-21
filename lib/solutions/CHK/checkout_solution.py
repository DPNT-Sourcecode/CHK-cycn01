
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # create dict of skus to consolidate them
        sku_dict = dict()
        for sku in skus:
            # get old and + 1
            if sku_dict.get(sku) is None:
                sku_dict.update({sku: 1})
            else:
                val = sku_dict.get(sku)
                sku_dict.update({sku: val+1})
                
        #check sku_dict is as expected
        print(sku_dict)

        #set up specials
        A_special = [3, 130]
        B_special = [2, 45]

        #set up base prices
        A_price = 50
        B_price = 30
        C_price = 20
        D_price = 15

        #calculate the price
        price = 0
        #TODO pretty sure I can streamline this significantly
        for key in sku_dict.keys():
            if key is "A":
                number = sku_dict.get(key)
                number_of_non_specials = number % A_special[0]
                price += number_of_non_specials * A_price
                price += ((number - number_of_non_specials)/A_special[0]) * A_special[1]
            if key is "B":
                number = sku_dict.get(key)
                number_of_non_specials = number % B_special[0]
                price += number_of_non_specials * B_price
                price += ((number - number_of_non_specials)/B_special[0]) * B_special[1]
            if key is "C":
                price += sku_dict.get(key) * C_price
            if key is "D":
                price += sku_dict.get(key) * D_price
            else:
                return -1

