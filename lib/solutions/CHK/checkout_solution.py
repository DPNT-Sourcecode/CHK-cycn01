
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
        # Ok there's definitely a way to do this with object-oriented programming to make this 1 check...
        #For now I'm just gonna functionise the more complex applications
        for key in sku_dict.keys():
            match key:
                case "A":
                    number = sku_dict.get(key)
                    price += self.two_tier_discount(A_price, A_special, A_special_2, number)
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
                    # This is basically the same as the basic B case, because 3Fs = a new price, and any remainders are added as normal.
                    number = sku_dict.get(key)
                    number_of_non_specials = number % F_special[0]
                    price += number_of_non_specials * F_price
                    price += ((number - number_of_non_specials)/F_special[0]) * F_special[1]
                case _:
                    return -1
                
        return int(price)
    
    def two_tier_discount(self, price, special1, special2, number):
        # mod the larger special to get remainder
        number_of_non_extra_specials = number % special2[0]
        print(number_of_non_extra_specials)
        # mod smaller special to get remainder of remainder
        number_of_non_specials = number_of_non_extra_specials % special1[0]
        # add items that don't get a special
        out_price = number_of_non_specials * price
        # add items that only get the smaller special
        out_price += ((number_of_non_extra_specials - number_of_non_specials)/special1[0]) * special1[1]
        # add items from the larger special
        out_price += ((number - number_of_non_extra_specials)/special2[0]) * special2[1]
        return out_price
    
    def get_free_by_other(self, price, special, other_special, number, other_number):
        # Apply the E discount by taking away any Bs that are made free by the Es
        if other_number is not None:
            number = number - (other_number // other_special)
        # Now we've gotten rid of the free Bs, we can continue as normal
        number_of_non_specials = number % special[0]
        out_price = number_of_non_specials * price
        out_price += ((number - number_of_non_specials)/special[0]) * special[1]
        return out_price



