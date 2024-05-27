# Prerequisites

- Python 3.9+
- Node 20+
- NPM 10.5.0
- WebScreenshots.csv

# Installation

The project itself is a **Python** project with a **Node** project within it.

## Python

1. Initiate a Python environment

```sh
python -m venv .venv
```

This would create a `.venv` file within the project.

2. Activate the environment

`Windows`

```sh
.venv\Scripts\activate
```

`Linux`

```sh
source venv/bin/activate
```

A preffix `(.venv)` should appear before the path, example:

`(.venv) C:\Users\user\BetterSEODataFactory>`

3. Install packages using `pip`

```sh
pip install -r requirements.txt
```

## Node

The Node project itself lives within `BetterSEODataFactory\Lighthouse`, and even done it is run by Python itself, it is needed to install the appropiate npm packages:

1. Go to the folder `BetterSEODataFactory/Lighthouse`

2. Install the packages

```sh
npm install
```

That should be it!

## WebScreenshots.csv

We used a dataset called `WebScreenshots.csv` in order to get curated plain URLs. If you have your own dataset make sure it is named like so and located at: `BetterSEODataFactory\Lighthouse\WebScreenshots.csv`. Or change the path within the code.

Also make sure it simple has a first row "WebPage", followed by one URL per row:

`WebScreenshots.csv`
```
WebPage
https://www.primevideo.com/
https://www.netflix.com/
https://medium.com/
```

# Execution

Simply run main.py

```sh
python main.py
```

That starts the scraping and Lighthouse process. It also creates some required output directories for the data to be written to.
