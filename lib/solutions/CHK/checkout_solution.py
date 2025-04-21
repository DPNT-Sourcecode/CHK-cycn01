
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

        #set up base prices
        A_price = 50
        B_price = 30
        C_price = 20
        D_price = 15
        E_price = 40
        F_price = 10

        #set up specials
        A_special = [3, 130]
        A_special_2 = [5, 200]
        B_special = [2, 45]
        E_special = 2
        F_special = [3, F_price * 2]

        #calculate the price
        price = 0
        #TODO pretty sure I can streamline this significantly
        for key in sku_dict.keys():
            match key:
                case "A":
                    number = sku_dict.get(key)
                    # mod the larger special to get remainder
                    number_of_non_extra_specials = number % A_special_2[0]
                    print(number_of_non_extra_specials)
                    # mod smaller special to get remainder of remainder
                    number_of_non_specials = number_of_non_extra_specials % A_special[0]
                    # add items that don't get a special
                    price += number_of_non_specials * A_price
                    # add items that only get the smaller special
                    price += ((number_of_non_extra_specials - number_of_non_specials)/A_special[0]) * A_special[1]
                    # add items from the larger special
                    price += ((number - number_of_non_extra_specials)/A_special_2[0]) * A_special_2[1]
                case "B":
                    number = sku_dict.get(key)
                    # Apply the E discount by taking away any Bs that are made free by the Es
                    if sku_dict.get("E") is not None:
                        no_of_Es = sku_dict.get("E")
                        number = number - (no_of_Es // E_special)
                    # Now we've gotten rid of the free Bs, we can continue as normal
                    number_of_non_specials = number % B_special[0]
                    price += number_of_non_specials * B_price
                    price += ((number - number_of_non_specials)/B_special[0]) * B_special[1]
                case "C":
                    price += sku_dict.get(key) * C_price
                case "D":
                    price += sku_dict.get(key) * D_price
                case "E":
                    # E specials have been applied in B case.
                    price += sku_dict.get(key) * E_price
                case "F":
                    #buy 2F get 1F free, but only in 3s.
                case _:
                    return -1
                
        return int(price)


