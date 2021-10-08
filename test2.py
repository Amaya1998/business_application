import numpy as np
fruits= np.array (['Banana','Pine-apple','Strawberry','Avocado','Guava','Papaya'])
print(fruits)

def insertionSort(fruits):
    for i in range(1, len(fruits)):   # 1 to length-1
        item = fruits[i]
                                # Move elements
                                # to right by one position
        f = i
        while f >0 and fruits[f-1] > item:
            fruits[f] = fruits[f-1]      # move value to right
            f -= 1
        fruits[f] = item          # insert at correct place
insertionSort(fruits)
print(fruits)
