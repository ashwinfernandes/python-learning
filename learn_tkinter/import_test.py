import blackjack

# from blackjack import *  # imports everything from the module blackjack except
# everything that begins with an '_' i.e. _deal_card() will not be imported and
# therefore cannot be used here

# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()

personal_details = ("Tim", 24, "Australia")

# using _ as a variable name when the value is not interesting and can be ignored
name, _, country = personal_details
print(name, country)
print(_)
