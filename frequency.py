import heapq


def find_freq(filename):
    found = {}
    with open(filename, "r") as file:
        for words in file:
            words = words.rstrip()
            if words not in found:
                found[words] = 1
            else:
                found[words] += 1

    return found


def find_list(dic_words, k):
    heap = []
    final_list = []

    for word, count in dic_words.items():
        tup = (count, word)

        if len(heap) < k:
            heapq.heappush(heap, tup)
        else:
            if count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, tup)

    while heap:
        final_list.append(heapq.heappop(heap))

    return final_list
