import pytest
import builtins
from unittest import mock
from portfolio import Portfolio

def main():
    test_init_portfolio()
    test_str_portfolio()
    test_deposit()



def test_init_portfolio():
    with mock.patch("builtins.input", lambda _: "MyPortfolio"):
        portfolio = Portfolio.get()
        assert portfolio.name == "MYPORTFOLIO"
        assert portfolio.capacity == 1
        assert portfolio.size is None
        assert portfolio.symbol is None
        assert portfolio.portfolio == {}
        assert portfolio.total == []
        assert portfolio.symbols == []


def test_str_portfolio():
    portfolio = Portfolio("My Portfolio")
    portfolio.portfolio = {"AAPL": 0.5, "TSLA": 0.5}
    assert portfolio.portfolio == {"AAPL": 0.5, "TSLA": 0.5}


def test_deposit():
    portfolio = Portfolio("My Portfolio")
    portfolio.deposit("AAPL", 100)
    assert portfolio.size == 1.0
    assert portfolio.symbol == "AAPL"
    assert portfolio.portfolio["AAPL"] == 1.0
    assert portfolio.total == [1.0]
    assert portfolio.symbols == ["AAPL"]
    # Invalid input type
    with pytest.raises(TypeError):
        portfolio.deposit("Invalid input type")
    # Cannot allocate negative or 0 %
    with pytest.raises(ValueError) as e:
        portfolio.deposit("AAPL", -100)
        assert e == "Cannot allocate negative or 0 %"
    # Cannot allocate over 100%
    with pytest.raises(ValueError) as e:
        portfolio.deposit("GOOG", 100)
        assert e == "Cannot allocate over 100%"
    # Ticker symbol already selected
    with pytest.raises(ValueError) as e:
        portfolio.deposit("AAPL", 50)
        assert e == "Ticker symbol already selected"
    # Ticker symbol cannot be empty
    with pytest.raises(ValueError) as e:
        portfolio.deposit("", 100)
        assert e == "Ticker symbol cannot be empty"
    # Percentage must be integer
    with pytest.raises(ValueError) as e:
        portfolio.deposit("IBM", "")
        assert e == "Please enter an integer value"

    # Ticker symbol cannot be a number or float
    with pytest.raises(ValueError) as e:
        portfolio.deposit(45, 30)
        assert e == "Ticker symbol cannot be a number or float"


if __name__ == "__main__":
    main()
