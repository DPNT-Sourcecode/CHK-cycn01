
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
        #print(sku_dict)
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |

        #set up base prices    
        prices = {
            "A": 50, #3A for 130, 5A for 200
            "B": 30, #2B for 45
            "C": 20,
            "D": 15,
            "E": 40, #2E get one B free
            "F": 10, #2F get one F free
            "G": 20,
            "H": 10, #5H for 45, 10H for 80
            "I": 35,
            "J": 60,
            "K": 70, #2K for 150    
            "L": 90,
            "M": 15,
            "N": 40, #3N get one M free
            "O": 10,
            "P": 50, #5P for 200
            "Q": 30, #3Q for 80
            "R": 50, #3R get one Q free
            "S": 30,
            "T": 20,
            "U": 40, #3U get one U free
            "V": 50, #2V for 90, 3V for 130
            "W": 20,
            "X": 90,
            "Y": 10,
            "Z": 50
        }

        #set up specials
        A_special = [3, 130]
        A_special_2 = [5, 200]
        B_special = [2, 45]
        E_special = 2
        F_special = [3, prices["F"] * 2]
        H_special = [5, 45]
        H_special_2 = [10, 80]
        K_special = [2, 120]
        M_special = [1, prices["M"]]
        N_special = 3
        P_special = [5, 200]
        Q_special = [3, 80]
        R_special = 3
        U_special = [4, prices["U"] * 3]
        V_special = [2, 90]
        V_special_2 = [3, 130]

        #calculate the price
        price = 0

        #Apply group discount first because we need to reduce the count of those from the dict
        number_in_group = sku_dict.get("S", 0) + sku_dict.get("T", 0) + sku_dict.get("X", 0) + sku_dict.get("Y", 0) + sku_dict.get("Z", 0)
        times_to_minus = number_in_group // 3
        for _i in range(times_to_minus):
            for _j in range(3):
                print(sku_dict)
                print(sku_dict.get("X"))
                # Go from most expensive first
                if sku_dict.get("X") is not None and sku_dict.get("X") != 0:
                    val = sku_dict.get("X")
                    sku_dict.update({"X": val-1})
                elif sku_dict.get("Z") is not None and sku_dict.get("Z") != 0:
                    val = sku_dict.get("Z")
                    sku_dict.update({"Z": val-1})
                elif sku_dict.get("S") is not None and sku_dict.get("S") != 0:
                    val = sku_dict.get("S")
                    sku_dict.update({"S": val-1})
                elif sku_dict.get("T") is not None and sku_dict.get("T") != 0:
                    val = sku_dict.get("T")
                    sku_dict.update({"T": val-1})
                elif sku_dict.get("Y") is not None and sku_dict.get("Y") != 0:
                    val = sku_dict.get("Y")
                    sku_dict.update({"Y": val-1})
        price += 45 * times_to_minus
        #TODO pretty sure I can streamline this significantly
        # Ok there's definitely a way to do this with object-oriented programming to make this 1 check...
        #For now I'm just gonna functionise the more complex applications
        for key in sku_dict.keys():
            match key:
                case "A":
                    number = sku_dict.get(key)
                    price += self.two_tier_discount(prices[key], A_special, A_special_2, number)
                case "B":
                    number = sku_dict.get(key)
                    price += self.get_free_by_other(prices[key], B_special, E_special, number, sku_dict.get("E"))
                case "C":
                    price += sku_dict.get(key) * prices[key]
                case "D":
                    price += sku_dict.get(key) * prices[key]
                case "E":
                    # E specials have been applied in B case.
                    price += sku_dict.get(key) * prices[key]
                case "F":
                    #buy 2F get 1F free, but only in 3s.
                    # This is basically the same as the basic B case, because 3Fs = a new price, and any remainders are added as normal.
                    number = sku_dict.get(key)
                    price += self.basic_special(prices[key], F_special, number)
                case "G":
                    price += sku_dict.get(key) * prices[key]
                case "H":
                    #5H for 45, 10H for 80
                    number = sku_dict.get(key)
                    price += self.two_tier_discount(prices[key], H_special, H_special_2, number)
                case "I":
                    price += sku_dict.get(key) * prices[key]
                case "J":
                    price += sku_dict.get(key) * prices[key]
                case "K":
                    #2K for 150  
                    number = sku_dict.get(key)
                    price += self.basic_special(prices[key], K_special, number)
                case "L":
                    price += sku_dict.get(key) * prices[key]
                case "M":
                    #3N get one M free
                    number = sku_dict.get(key)
                    price += self.get_free_by_other(prices[key], M_special, N_special, number, sku_dict.get("N"))
                case "N":
                    price += sku_dict.get(key) * prices[key]
                case "O":
                    price += sku_dict.get(key) * prices[key]
                case "P":
                    #5P for 200
                    number = sku_dict.get(key)
                    price += self.basic_special(prices[key], P_special, number)
                case "Q":
                    #3Q for 80
                    #3R get one Q free
                    number = sku_dict.get(key)
                    price += self.get_free_by_other(prices[key], Q_special, R_special, number, sku_dict.get("R"))
                case "R":
                    #Handled by Q
                    price += sku_dict.get(key) * prices[key]
                case "S":
                    price += sku_dict.get(key) * prices[key]
                case "T":
                    price += sku_dict.get(key) * prices[key]
                case "U":
                    #3U get one U free
                    number = sku_dict.get(key)
                    price += self.basic_special(prices[key], U_special, number)
                case "V":
                    #2V for 90, 3V for 130
                    number = sku_dict.get(key)
                    price += self.two_tier_discount(prices[key], V_special, V_special_2, number)
                case "W":
                    price += sku_dict.get(key) * prices[key]
                case "X":
                    price += sku_dict.get(key) * prices[key]
                case "Y":
                    price += sku_dict.get(key) * prices[key]
                case "Z":
                    price += sku_dict.get(key) * prices[key]
                case _:
                    return -1
                
        return int(price)
    
    def basic_special(self, price, special, number):
        number_of_non_specials = number % special[0]
        out_price = number_of_non_specials * price
        out_price += ((number - number_of_non_specials)/special[0]) * special[1]
        return out_price
    
    def two_tier_discount(self, price, special1, special2, number):
        # mod the larger special to get remainder
        number_of_non_extra_specials = number % special2[0]
        #print(number_of_non_extra_specials)
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
    
    # def group_discount(self, items_in_group, group_size, group_price, number price, group_done):
    #     number_of_items = 0
    #     for item in items_in_group:
    #         number_of_items += item
    #     number_of_non_discounts = number_of_items % group_size
    #     out_price = number_of_non_discounts * price
    #     number_of_group_discounts = number_of_items - number_of_non_discounts
    #     out_price += number_of_group_discounts * group_price
    #     return out_price, number_of_group_discounts
