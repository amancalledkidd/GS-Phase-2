def get_most_common_letter(text):
    counter = {}
    text = text.replace(" ", "")

    for char in text:
        # print(f"character: {char}")
        counter[char] = counter.get(char, 0) + 1
        # print(f"This is counter dictionary {counter}")
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    return letter


print(get_most_common_letter("the roof, the roof, the roof is on fire!"))


# print(f"""
# Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# Expected: o
# Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# """)