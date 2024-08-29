print()
print(">>>Colecciones")
print()

def pyrramid_sum(lower,upper,margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
         result = lower + pyrramid_sum(lower + 1, upper, margin + 4)
         print(blanks, result)
         return result

pyrramid_sum(1,4)     
    