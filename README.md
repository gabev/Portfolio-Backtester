# Portfolio Backtester
 Video Demo:  https://youtu.be/LMbeaGuYC5g
    
    
## Description :


![](/img/photo_2023-11-13_19-29-45.jpg)

 The Portfolio Backtester is a tool for quantitative analysts (quants) and portfolio managers who want to gain deeper insights into their investment portfolios. Built around Quantstats and YFinance library, with its advanced analytical capabilities, it enables users to evaluate their portfolio's performance against various benchmarks and identify potential areas of improvement.

One of the key features of QuantStats is its ability to perform portfolio profiling. This involves analyzing various aspects of a portfolio, such as asset allocation, measures of volatility, value at risk (VaR), diversification and risk exposure, to provide valuable insights into how well it aligns with the investor's objectives and constraints. By understanding these factors, investors can make informed decisions about whether to adjust their portfolio or leave it unchanged.

Overall, the Portfolio Backtester in conjunction with QuantStats Python library is an essential tool for any quantitative analyst or portfolio manager looking to improve their investment strategies and achieve better outcomes for their clients.

## Features :

- Creates your own personalized portfolio for testing
- Downloads financial info from Yahoo Finance website
- Calculates 71 Key Performance Metrics as well prepare html charts for easy viewing
- Tests the performance against S&P 500, Dow Jones Industrial or NASDAQ Composite indexes
- Timeframes can be selected in the range of 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd or max
- Results are displayed within an html file
- All reports are saved localy for later review and analysis

## Prerequisites :

Before you can start using the Portfolio Backtester, make sure you have the following prerequisites installed on your system:


- Python 3.10 and higher
- termcolor
- pyfiglet
- [yfinance](https://github.com/ranaroussi/yfinance)
- [quantstats](https://github.com/ranaroussi/quantstats)
- datetime
- pytest
- unittest
- builtins
- ipython (for some reasons running under Python 3.12 raises an error complaining about IPython module not found)

You can install the above libraries by running pip install -r requirements.txt at the command prompt.


#### Files contained within the project :
    
- project.py - main file of the project
- portfolio.py - contains the Portfolio class and classmethods
- test_project.py - the unit tests for the functions within the project.py
- test_portfolio.py - the unit test for methods within portfolio.py
- requirements.txt - contains the list of all external libraries needed
- README.txt - this project description file

#### ** project.py :

- get_today_date() -returns refactored date (used in the naming of the report file)
- get_symbol(symbol) - returns stock symbol if valid. Uses yf.Ticker from yfinance library
- get_portfolio_name() - returns the name of the portfolio
- allocated_portfolio(portfolio) - returns a dictionary containing the stock symbols and the percentage allocate
- get_index_fund_symbol() - returns the symbol of the selected index fund
- generate_output(symbol, index_fund, date) - generates the name of the report file
- generate_link(symbol, index_fund, date) - generates the path to the report file
- generate_title(symbol, index_fund) - returns the title of the report

#### ** portfolio.py :

- class Portfolio - instantiate the portfolio object
- def symbol(self, symbol) - the setter for the symbol
- def deposit(self, symbol, value) - 
- @classmethod def get(cls) - sets the portfolio name

#### ** test_project.py :

- contains all the test functions for validation and error checking

#### ** test_portfolio.py:

- contains all the test for the methods contained in portfolio.py

#### ** requirements.txt :

- contains all the external libraries needed for the project

#### ** README.md :

- this file





## Instalation :

#### 1. Create a Python virtual environment (optional but recommended) :
```
python3 -m venv venv
source venv/bin/activate 
```

#### 2. Clone this repository to your local machine :
```
git clone https://github.com/gabev/Portfolio-Backtester
cd Portfolio-Backtester
```

### 3. Create a folder named "reports" inside the project folder:

```
mkdir reports 
```
> [!IMPORTANT]
> The folder should be located in the directory where the project.py file will be run.


#### 3. Install the required Python packages by running :
```
pip3 install -r requirements.txt
```

## Usage :

To use Portfolio Backtester follow these steps:

1. Start by running the application :
    ```
    python3 project.py
    ```

2. Give a name to your Portfolio :

    ![](/img/photo_2023-11-14_18-54-18.jpg)


3. Follow the promp and start adding stock symbols :
    
    ![](/img/photo_2023-11-14_18-55-51.jpg)
    

4. Allocate a percentage to the stock :

    ![](/img/photo_2023-11-14_18-58-43.jpg)

5. Continue to allocate other assets until your portfolio is full :

    ![](/img/photo_2023-11-14_19-01-35.jpg)

6. Enter a period for your portfolio performance and the Index Fund Symbol
   against which you wanna compare the performance against. Valid timeframe periods are 
   1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd or max :

    ![](/img/photo_2023-11-14_19-03-09.jpg)

7. Portfolio Backtester will start downloading data from Yahoo Finance and calculate the performance metrics.

    ![](/img/photo_2023-11-14_19-11-30.jpg)

8. Once finished a webpage containing the results will automatically be open in your default browser.
   To run a test for another portfolio type yes(y) to continue or no(n) to exit.

    ![](/img/photo_2023-11-14_19-18-48.jpg)

    To view your backtests later on just open the "reports" folder. The html files are named and saved using the following convention: portfolio name-vs-Index Fund Symbol_year_month_day_hour-minutes_.html


## Testing :

 In order to verify the accuracy of each function within the project, there are a series of tests included in the `test_project.py` file. These tests utilize both the `unittest` and `pytest` libraries to ensure comprehensive coverage and reliable results. Before running the tests, it is important to install both libraries. To run the tests, in the comman prompt or terminal navigate to the project directory and run the command : `pytest -v test_project.py` and `pytest -v test_portfolio.py`.