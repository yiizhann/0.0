name: Auto Push Heat Index
on:
  schedule:
    - cron: "0 1,3,5,7 * * *"
  workflow_dispatch:

jobs:
  push_heat:
    runs-on: ubuntu-latest
    env:
      CHANNEL_ACCESS_TOKEN: ${{ secrets.CHANNEL_ACCESS_TOKEN }}
      GROUP_ID: ${{ secrets.GROUP_ID }}
    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y chromium-driver
        pip install -r requirements.txt

    - name: Run bot
      run: python main.py
