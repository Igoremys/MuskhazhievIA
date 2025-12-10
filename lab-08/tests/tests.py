from greedy_algorithms import *

def test_interval():
    assert len(interval_scheduling([(1,3), (2,4), (3,5)])) == 2

def test_knapsack():
    val, _ = fractional_knapsack([(60,10), (100,20), (120,30)], 50)
    assert abs(val - 240.0) < 1e-5

def test_huffman():
    codes, _ = huffman_coding({'a':5, 'b':9, 'c':12})
    assert len(codes) == 3