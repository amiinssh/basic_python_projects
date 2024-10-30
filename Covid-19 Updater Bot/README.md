Covid-19 Updates Notifier

This Python script provides periodic desktop notifications with the latest Covid-19 statistics (cases, deaths, and recoveries) using a toast notification on Windows.
Prerequisites

    Python 3 installed
    Libraries: Install required libraries with:

    bash

    pip install requests win10toast

How It Works

The script:

    Fetches Covid-19 statistics from an API.
    Displays a Windows toast notification with the latest updates.
    Updates every 60 seconds.

Usage

    Run the script:

    bash

    python covid_notifier.py

    Notifications will appear every minute with the latest statistics.

Notes

    Ensure a stable internet connection for accurate data retrieval.
    The API endpoint used may experience downtime.
