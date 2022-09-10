import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

cards = []
card_list = sorted(list(map(int, sys.stdin.readline().split())))

for card in card_list:
    heapq.heappush(cards, card)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)
print(sum(cards))
