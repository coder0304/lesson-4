amount= int(input("please enter the amount for withdraw:"))
note_1= amount/100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("notes in 100 rupee",note_1)
print("notes in 50 rupee",note_2)
print("notes in 10 rupee",note_3)