from portfolio import Portfolio
from termcolor import cprint
from pyfiglet import figlet_format
import yfinance as yf
import quantstats as qs
from datetime import datetime
import os, sys, time, webbrowser, re, warnings

warnings.filterwarnings("ignore", category=FutureWarning)

MAX_PERIOD_SIZE = (
    "1d",
    "5d",
    "1mo",
    "3mo",
    "6mo",
    "1y",
    "2y",
    "5y",
    "10y",
    "ytd",
    "max",
)



# Getting today's date
def get_today_date():
    now = datetime.now()
    date = now.isoformat("_", "minutes")
    date = re.sub(r"[:]", "-", date)
    return date


def get_symbol(symbol):
    ticker = yf.Ticker(symbol)
    pd_frame = ticker.history(interval="1d")
    if not pd_frame.empty:
        cprint(f"{symbol} is on Yahoo Finance..", "green")
        return symbol
    else:
        print(f"No data available for {symbol}.")
        return None



def get_portfolio_name():
    portfolio_name = input("Name your Portfolio: ").upper()
    return portfolio_name


def allocated_portfolio(portfolio):
    while True:
        try:
            while True:
                cprint("Input Stock/Index Symbol(ex: AAPL ..): ", "yellow")
                try:
                    symbol = input().upper()
                    stock_symbol = get_symbol(symbol)
                    if stock_symbol != None:
                        break
                except Exception as e:
                    cprint(e, "red")
                    cprint("Select again", "yellow")

            stock_percentage = int(input("Input Percentage: "))
            portfolio.deposit(stock_symbol, stock_percentage)
        except Exception as e:
            cprint(e, "red")
            cprint("Select again", "yellow")

        if sum(portfolio.total) < 1:
            cprint(
                f"{((1-sum(portfolio.total))*100):.2f}% of portfolio still available",
                "green",
            )
            print("Add another stock")
            continue

        elif sum(portfolio.total) == 1:
            cprint("Portfolio is now fully allocated", "green")
            return portfolio



def get_index_fund_symbol():
    cprint(
        f"Valid index fund symbols:\nS&P500 = ^GSPC,\nDow Jones Industrial Average = ^DJI,\nNASDAQ Composite = ^IXIC",
        "yellow",
    )
    index_list = ["^GSPC","^DJI","^IXIC"]
    while True:
        index_fund_name = input("Input Index Fund Symbol: ").upper()
        if index_fund_name in index_list:
            return index_fund_name
        else:
            cprint("Please enter a valid Index Fund Symbol", "red")
            continue


def generate_output(symbol, index_fund, date):
    output = "reports/" + symbol + " vs. " + index_fund + "_" + date + "_" + ".html"
    return output


def generate_link(symbol, index_fund, date):
    link = "/reports/" + symbol + " vs. " + index_fund + "_" + date + "_" + ".html"
    return link


def generate_title(symbol, index_fund):
    title = symbol + "-vs-" + index_fund
    return title


def main():

    cprint(
        figlet_format("Portfolio Backtester", font="standard", width=120),
        "yellow",
        attrs=["bold"],
    )

    cprint(
        """          
                        An in-depth analytics and risk metrics tool,
            built with QuantStats Python library that performs portfolio profiling,
        allowing quants and portfolio managers to better understand their performance.
            """
    )
    print()

    while True:
        portfolio = Portfolio.get()
        p = allocated_portfolio(portfolio)
        print(f"{p.name}-{p.portfolio}")
        tickers = p.portfolio
        date = get_today_date()
        while True:
            cprint(
                    "The following are valid periods:\n1d,5d,\n1mo,3mo,6mo,\n1y,2y,5y,10y,ytd,max",
                    "yellow",
                )
            input_period = input("Enter a period: ")
            if input_period not in MAX_PERIOD_SIZE:
                continue
            period = input_period
            index_fund = get_index_fund_symbol()
            title = generate_title(portfolio.name, index_fund)
            output = generate_output(portfolio.name, index_fund, date)
            link = generate_link(portfolio.name, index_fund, date)
            report = qs.utils.make_index(tickers, period=period)
            cprint("Downloading data from Yahoo Finance ...", "green")
            time.sleep(2.5)
            cprint("Generating report ...", "green")
            time.sleep(1)
            qs.reports.html(report, index_fund.lower(), title=title, output=output)
            cprint("Generating webpage ...", "green")
            time.sleep(2.5)
            webbrowser.open("file://" + os.path.abspath(os.getcwd()) + link)
            cprint("Backtest another portfolio? (yes/no or y/n)", "yellow")
            choice = input().lower()
            if choice == "yes" or choice == "y":
                continue
            else:
                sys.exit(
                    cprint(
                        "\u2764\uFE0F  Thank you for using our program. Happy trading ! \u2764\uFE0F  ",
                        "green",
                        attrs=["bold"],
                    )
                )


if __name__ == "__main__":
    main()
