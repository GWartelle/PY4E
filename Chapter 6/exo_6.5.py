text = "X-DSPAM-Confidence:    0.8475"
nbr_place = text.find("0.")
nbr = float(text[nbr_place:])
print(nbr)