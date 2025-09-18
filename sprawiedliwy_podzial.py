import heapq



print("podaj liczbe przedmiotow")
n = int(input())
        

print("podaj wartosci dla Bajtyny, oddzielone spacjami")
a = list(map(int, input().split()))
        

print("podaj wartosci dla Bitka, oddzielone spacjami")
b = list(map(int, input().split()))
   

result = [0] * n
bajtyna_heap = [] 
bitek_heap = []    
suma_a_dla_a = 0
suma_b_dla_b = 0
suma_a_dla_b = 0
suma_b_dla_a = 0

items = []
for i in range(n):
    items.append((a[i], b[i], i))
        
for val_a, val_b, index in items:
    if val_a > val_b:
        result[index] = 0
        heapq.heappush(bajtyna_heap, (val_b, val_a, index))
        suma_a_dla_a += val_a
        suma_b_dla_a += val_b
    elif val_b > val_a:
        result[index] = 1
        heapq.heappush(bitek_heap, (val_a, val_b, index))
        suma_b_dla_b += val_b
        suma_a_dla_b += val_a
    else:
        if suma_a_dla_a <= suma_b_dla_b:
            result[index] = 0
            heapq.heappush(bajtyna_heap, (val_b, val_a, index))
            suma_a_dla_a += val_a
            suma_b_dla_a += val_b
        else:
            result[index] = 1
            heapq.heappush(bitek_heap, (val_a, val_b, index))
            suma_b_dla_b += val_b
            suma_a_dla_b += val_a


while suma_a_dla_a < suma_a_dla_b - (bitek_heap[0][0] if bitek_heap else float('inf')):
    a_val, b_val, idx = heapq.heappop(bitek_heap)
        
    suma_a_dla_a += a_val
    suma_b_dla_a += b_val
    suma_a_dla_b -= a_val
    suma_b_dla_b -= b_val
    result[idx] = 0
        
    heapq.heappush(bajtyna_heap, (b_val, a_val, idx))


while suma_b_dla_b < suma_b_dla_a - (bajtyna_heap[0][0] if bajtyna_heap else float('inf')):
    b_val, a_val, idx = heapq.heappop(bajtyna_heap)
        
    suma_b_dla_b += b_val
    suma_a_dla_b += a_val
    suma_b_dla_a -= b_val
    suma_a_dla_a -= a_val
    result[idx] = 1
        
    heapq.heappush(bitek_heap, (a_val, b_val, idx))

print(*result) 