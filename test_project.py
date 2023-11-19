import pytest
import builtins
from unittest import mock
from datetime import datetime, timedelta
from project import (
    get_symbol,
    get_today_date,
    generate_output,
    generate_link,
    generate_title,
    get_index_fund_symbol,
)
from portfolio import Portfolio



def main():
    test_get_symbol()
    test_get_today_date()
    test_get_today_date_no_seconds()
    test_get_today_date_valid()
    test_generate_output()
    test_generate_link()
    test_generate_title()
    test_get_portfolio_name()
    test_get_index_fund_symbol()
    test_allocated_portfolio()


def test_allocated_portfolio():
    pass


def test_get_portfolio_name():
    with mock.patch("builtins.input", lambda _: "MyPortfolio"):
        portfolio = Portfolio.get()
        assert portfolio.name == "MYPORTFOLIO"


def test_get_index_fund_symbol():
    with mock.patch.object(builtins, "input", lambda _: "^GSPC"):
        assert get_index_fund_symbol() == "^GSPC"


def test_generate_output():
    symbol = "AAPL"
    index_fund = "^GSPC"
    date = "2023-11-06_18-22"
    assert (
        generate_output(symbol, index_fund, date)
        == "reports/AAPL vs. ^GSPC_2023-11-06_18-22_.html"
    )


def test_generate_link():
    symbol = "AAPL"
    index_fund = "^GSPC"
    date = "2023-11-06_18-22"
    assert (
        generate_link(symbol, index_fund, date)
        == "/reports/AAPL vs. ^GSPC_2023-11-06_18-22_.html"
    )


def test_generate_title():
    symbol = "AAPL"
    index_fund = "^GSPC"
    assert generate_title(symbol, index_fund) == "AAPL-vs-^GSPC"


def test_get_today_date():
    # Test edge cases where the minute is 59 or 60
    now = datetime.now()
    now.replace(minute=59)
    expected_result = now.isoformat("_", "minutes").replace(":", "-")
    assert get_today_date() == expected_result

    with pytest.raises(ValueError):
        now.replace(minute=60)
        expected_result = (
            (now + timedelta(minutes=1)).isoformat("_", "minutes").replace(":", "-")
        )
        assert get_today_date() == expected_result


def test_get_today_date_no_seconds():
    # Test that the function returns a string in the format YYYY-MM-DDTHH-mm when seconds are zero
    now = datetime.now()
    now.replace(second=0)
    expected_result = now.isoformat("_", "minutes").replace(":", "-")
    assert get_today_date() == expected_result


def test_get_today_date_valid():
    # Test that the function returns a string in the format YYYY-MM-DDTHH-mm
    assert isinstance(get_today_date(), str)
    assert len(get_today_date()) == 16
    assert get_today_date().startswith(
        "20"
    )


def test_get_symbol():
    # Test a valid symbol
    assert get_symbol("AAPL") == "AAPL"
    # Test invalid symbol
    assert get_symbol("Not Valid") == None


if __name__ == "__main__":
    main()
