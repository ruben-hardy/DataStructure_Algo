import requests
import json


class Sandbox:
    def __init__(self):
        pass
    
    def LargestSeq(self, seq):
        self.seq = seq
        left = right = 0
        seqDict = {x:0 for x in self.seq}
        for num in self.seq:
            if seqDict[num] == 0:
                left_count = num - 1
                right_count = num + 1
                while left_count in seqDict:
                    left_count -= 1
                    seqDict[num] = 1
                left_count += 1
                while right_count in seqDict:
                    seqDict[num] = 1
                    right_count += 1
                right_count -= 1
                if (right - left) <= (right_count - left_count):
                    left = left_count
                    right = right_count
        return [right, left]

    def NumCoins(self, cents, values = [25, 10, 1]):
        original_value = cents
        reference = {25: 'Quarter', 10: 'dime', 5: 'nickel', 1: 'cent'}
        balance = dict()
        rem = 0
        for value in values:
            balance[reference[value]] = cents // value
            if cents % value == 0:
                break
            else:
                cents = cents % value
        if 'cent' not in balance:
            return balance
        elif balance['cent'] >= 5:
            balance = self.NumCoins(original_value, [10, 1, 25])
            return balance
        return balance
    
    def reverse(self, x):
        print(x[::-1])

    def minimum(self, x):
        min = x[0]
        min2 = x[1]
        for i in x:
            if i < min:
                min2 = min
                min = i
            elif (i<min2) and (i > min):
                min2 = i
        print(min, min2)

    def NthMinimum(self, lst, m):
        left_array = list()
        right_array = list()
        index = 0
        for i in range(len(lst)):
            if lst[i] < lst[index]:
                left_array.append(lst[i])
            elif lst[i] > lst[index]:
                right_array.append(lst[i])
            else:
                continue
        print(left_array + [lst[index]] + right_array)

    def fibonacci(self, val):
        a = 0
        b = 1
        for i in range(val):
            print(a, end=' ')
            a, b = b, a+b
        
    def api_testing(self, url):
        
        return requests.get(url)



            


    




run = Sandbox()
#run.minimum([3, 2, 5, 6])

#run.NthMinimum([10, 2, 5, 6, 3, 11, 0], 3)
resp = run.api_testing('https://jsonplaceholder.typicode.com/posts')
print(resp.status_code)
json_resp = json.loads(resp.text)
for i, item in enumerate(json_resp):
    print()
    print(i, item['title'])

