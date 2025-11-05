🏦 Massive.com Ticker Extractor

This project retrieves a comprehensive list of ticker symbols (stocks, indices, forex, and crypto) from the Massive.com
 REST API and exports them into a structured CSV file.

It handles pagination, API rate limits, and ensures robust error handling while fetching market data.
(Since I was using the Free subscription I had a limit of the number of API calls)

🚀 Features

Fetches ticker symbols across multiple asset classes (stocks, indices, forex, crypto).

Handles pagination automatically using the next_url field.

Includes rate-limit protection with automatic retry logic.

Exports data cleanly to a .csv file for analysis.

Built with Python and uses the Massive.com REST API.

🧰 Tech Stack

Language: Python 

Libraries:

requests — for API calls

dotenv — to load environment variables

csv — for exporting data
