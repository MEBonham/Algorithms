#!/usr/bin/python

import argparse

def find_max_profit(prices):
    profit = min(prices) - max(prices)
    for buy_index in range(len(prices)):
        for sell_index in range(buy_index + 1, len(prices)):
            if prices[sell_index] - prices[buy_index] > profit:
                profit = prices[sell_index] - prices[buy_index]
    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))