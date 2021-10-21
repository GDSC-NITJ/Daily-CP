import json

with open('Question.json') as b:
    bdata = json.load(b)


print("---Begineer Cp----")

blink1 = input("Enter Link 1: ")
blink2 = input("Enter Link 2: ")

print("---Intermediate Cp----")

ilink1 = input("Enter Link 1: ")
ilink2 = input("Enter Link 2: ")


i = bdata['Day Count']+1

bdata['Day Count'] = i

bdata.update(
    {f"Day {i}": {
        "begineer": {
            "Q1": blink1,
            "Q2": blink2
        },
        "intermediate": {
            "Q1": ilink1,
            "Q2": ilink2
        }
    }
 }
)

with open('Question.json', 'w') as b1:
    json.dump(bdata, b1)
