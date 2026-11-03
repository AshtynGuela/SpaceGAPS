# AgriForesight

**Current focus: the farm assistant.** Tap **Ask for help** on any page to check weather, compare crop options, update crop/stage details and save notes. [Assistant setup and limits](docs/ASSISTANT.md). Simulations are retired from the app; older guides below may still describe the previous water-planning work.
AI-GENERATED CONTENT INCOMING

A small farm-planning app built around Bicol. Check, try  watering plan, compare crops for the next season, and keep field notes (no func).

Runs locally with Python, Flask and SQLite. UI is plain HTML, CSS and JavaScript.

## Run it

On this Windows setup, double-click **START-AGRIFORESIGHT.cmd**. Keep the terminal window open and visit [the app](http://127.0.0.1:5000).

Or run this from the project folder:

```powershell
.\.venv\Scripts\python.exe app.py
```

To stop it, press Ctrl+C in that terminal. After changing Python files, restart the app. After changing the screens, refresh the browser.

For a fresh setup:

```powershell
python -m venv .venv
python -m pip --python .\.venv\Scripts\python.exe install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

The checked-in requirements pin Flask, requests and NumPy. Weather downloads need internet. The current weather integrations do not require an API key; check the providers’ terms before deploying a public or commercial app.

## Start here

1. Open **My farm & soil**. Save your farm location, crop, stage, water source and area. Leave soil readings blank if you do not have them.
2. Open **Forecasts** and update the weather. The usual forecast covers seven days. The separate **30-day outlook** gives a broader planning view.
3. In **Crop plans**, tell the app about drainage and choose **Find options for my farm**. Read the reasons and checks before picking a crop.
4. In **Simulations**, try a rain change or an extra watering. Water is entered in litres for the whole saved farm.
5. Use **Choose past dates** to explore up to 366 historical days. You can edit individual weather records or import a CSV.
6. Use **Field journal** for notes. These are saved for later work; they do not train the models or change the advice.

## What works, and what still needs work

| Area | What it does today |
| --- | --- |
| Farm location | Finds a Philippine town/province from saved boundary maps. It does not measure your parcel or establish ownership. |
| Past weather | Downloads NASA POWER or ERA5 data, accepts CSV records, and supports edits with restore copies. |
| App forecast | Compares regression with a 14-day average for a seven-day forecast. Past-date tests can cover a year. |
| Provider forecast | Loads seven-day Open-Meteo weather. A separate ECMWF EC46 feed supplies the 30-day outlook. |
| Crop suggestions | Uses explainable rules for crop history, drainage, terrain, water access and fresh short-range weather. |
| Planting calendar | Makes a draft schedule from your chosen date and crop duration. It does not find an optimal planting date. |
| Water plans | Compares daily soil-water or rice pond-water calculations using the settings you enter. |
| Soil | Stores pH, NPK and ash observations. It does not diagnose deficiencies, ash chemistry or microbiome health. |
| Offline | Keeps saved screens and queues notes. Calculations still need the local Flask server running. |

This is a single-farm prototype. There are no accounts, multi-farm permissions or production hosting setup. SARAi and PAGASA are reference links, not connected data feeds. SMS was removed from the scope.

Crop rankings are starting points for discussion, not locally validated suitability scores. The 30-day outlook is a broad area estimate. Its live download and the newer crop-planning screens still need a complete browser and field check.

## Docs

- [Using the app](docs/USER_GUIDE.md): everyday steps, dates, offline use and common problems.
- [How the project fits together](docs/DEVELOPMENT.md): files, storage, API routes and checks.
- [How the numbers work](docs/METHODS.md): forecasting, water calculations and crop ranking rules.
- [Learning guide](LEARNING_GUIDE.md): a practical route through the code.
- [Verification notes](docs/VERIFICATION.md): recorded checks and what they do not prove.
- [Boundary data](data/boundaries/README.md): location-data sources and licensing.

Older implementation notes remain in `docs/REFINEMENT_REPORT.md`, `docs/OCTOBER_FIXES.md` and `docs/FARMER_VIEW.md`. They describe earlier versions; use the guides above for the current behaviour.

## Your data

The local database is `instance/farm.sqlite3`. Stop the server before copying it for a backup. You can use the `AGRIFORESIGHT_DB` environment variable to choose another database file.

Browser storage holds the last dashboard and unsynced notes. Clearing browser storage can remove those pending notes. Keep using the same address and port: browsers treat different ones as separate places.

The JSON export contains the last browser state and pending notes. It is not a complete database backup or restore tool.

## Run the checks

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
node --check static/app.js
node --check static/sw.js
```

Node is only needed for those JavaScript syntax checks, not to run the app. The latest recorded suite passed 53 tests. A passing test suite does not establish real farm accuracy.
