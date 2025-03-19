import pytest  # Pytest framework import karna zaroori hai
from app import add  # test_app.py se add function import kar rahe hain

def test_add():
    assert add(2, 3) == 5  # Yeh test pass hona chahiye
    assert add(-1, 1) == 0  # Negative case check kar raha hai
    assert add(0, 0) == 0  # Zero case check ho raha hai

# Agar aur bhi functions hain to unke liye alag test likhein
