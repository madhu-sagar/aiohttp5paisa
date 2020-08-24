# aiohttp5paisa

Asychronous Python client for 5paisa.com REST API built with aiohttp. 

Check the /docs folder for more detailed information.

INSTALLATION :


USAGE: 


Rename .env.template to .env and fill the values

Refer the /examples folder

In brief :

* Can integrate this library in your complete trading system if you want to use 5paisa as an execution platform.
* Standalone tool to fetch marketfeed as it is offered for free curently.
* Use this library in a standalone format so as to place stoploss order if maximum loss is crossed for example. See /examples for an example.

MOTIVATION:

Since a lot of tools are available in Python for scientific and R&D purpose, it makes sense to have the complete trading system in single language like Python.
The present http packages are blocking in nature, hence hinder the fast I/O that framework like node.js provide. Hence the use of aiohttp that provides similar concurrent capabilities like that of node.js.

UPDATES :
This library is part of the trading tools currently being built in-house. Except some lag in updates as things are done in priority.

DISCLAIMER:
Absolute no warranty is provided by the author and the user using the library accepts complete responsibility for all liabilities that arise from the usage of the library.
