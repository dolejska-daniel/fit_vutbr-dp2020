# Master's Thesis / Diplomová práce
Overlay networks (like Tor or I2P) create a suitable environment for criminality to thrive on the Internet.
Dark marketplaces (a.k.a. cryptomarkets) are one such example of criminal activities.
They act as an intermediary in the trade of illegal goods and services.
This project focuses on forensic analysis of such web services and subsequent extraction of non-trivial information about the realised orders and payments from selected marketplaces.

The main goal is to pinpoint the time interval when an order has been completed on selected marketplaces and its following correlation with cryptocurrency blockchains.
The implemented program provides fully automated non-stop monitoring of selected cryptomarkets.
That, under certain conditions, allows detection of realised purchases, detailed product and vendor monitoring and collection of various meta-data entries.

Law enforcement agencies can use acquired data as support evidence regarding the operation of selected cryptomarkets and their vendors.
The obtained information can also indicate current trends in products supply and demand.

## Thesis Assessment ([official page](https://www.vutbr.cz/en/students/final-thesis/detail/136844))
| Type                  | Grade | Description                                   |
|-----------------------|-------|-----------------------------------------------|
| Supervisor assessment	| **A**	| [PDF](_assessment/supervisor.pdf) _in Czech_  |
| Reviewer assessment	| **A**	| [PDF](_assessment/reviewer.pdf) _in Czech_    |
| Defended grade		| **A**	| 												|


## Relevant Repositories
| Name                                                                                   | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| [TorScraper](https://github.com/dolejska-daniel/torscraper)                            | Configurable crawling/scraping framework. |
| [Result Analyser](https://github.com/dolejska-daniel/torscraper-analysis)              | Blockchain transaction correlator.        |
| [Darkmarket Plugins](https://github.com/dolejska-daniel/torscraper-darkmarket-plugins) | Cryptomarket-specific plugin modules.     |
