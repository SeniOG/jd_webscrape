# Job Site Web Scrape

Not intended for financial gain or any professional use. The project was intended for personal experience and coding practice only.

This script is designed to visit and collect job vacancy posts from the Totaljobs website. 

## Installation
Requires python3, selenium and chromedriver to be installed within directory. Chromedriver-mac-x64 was used when creating script.

## Usage
mac user: python3 totaljobs.py

win user: totaljobs.py

User must mke sure the url is the results of a job search, ie job description criteria should be manually entered into website search engine. The results page of this search, should be starting point for this script.

Keep an eye on the CLI for prompts to remove pop ups. When pop ups are cleared, press ENTER in the CLI. The CLI also provides additional updates for script progress. 

If the CLI read 'check IP', it is recommended to change your computer's IP address before conntinuing by pressing ENTER in the CLI. When the 'check IP' prompt appears, the current job desription will not be included in the final data file.

The custom pause function requires two numbers, which will then generate a random number between the provided numbers. This random number will be the duration of the pause, in seconds.

Two CSV files are created. The first is created gradually throughout the script duration. The other is created at the end. They should be identical.

## License
Creative Commons Attribution-NonCommercial (CC BY-NC)

*** NOT FOR COMMERCIAL USE ***

See LICENSE file for further details.