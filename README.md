# 20250903_Bosch_PyAdv

## References
* [Pep Index](https://peps.python.org/#)
* [Style Guide for Python](https://peps.python.org/pep-0008/)
* [Zen of Python](https://peps.python.org/pep-0020/)
* [Lexical Analysis](https://docs.python.org/3.11/reference/lexical_analysis.html#lexical-analysis)
    * [Escape Sequences](https://docs.python.org/3.11/reference/lexical_analysis.html#escape-sequences)
    * [Format Specifications](https://docs.python.org/3.11/library/string.html#format-specification-mini-language)
* [Virtual Environments using __*'venv'*__ ](https://docs.python.org/3/library/venv.html#module-venv)
* [Standard Encodings](https://docs.python.org/3/library/codecs.html)
* [Built-in Open Method](https://docs.python.org/3/library/functions.html#open)
* [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
    * [Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [operator - As fucntions](https://docs.python.org/3/library/operator.html#module-operator)
* Concurrency topic for further reading (if interested):
    * Synchronisation of Threads and Processes
    * Pools and methods (apply, map, and the async versions of these)
    * Executors
    * concurrent.Future
    * couroutines
    * Event loops
    * Gather
    * Asyncio libraries (aiohttp, aiofiles) 
    * https://github.com/python/asyncio
    * https://github.com/aio-libs
* [FastAPI](https://fastapi.tiangolo.com/)
    * [Concurrency Support for third party libraries](https://fastapi.tiangolo.com/async/?h=third+party+librari#in-a-hurry)
    * [HTTP Response codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
    * [Response - Change Status Code](https://fastapi.tiangolo.com/advanced/response-change-status-code/#use-a-response-parameter)
    * [HTTP Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)


## Snippets
* Virtual Enviroments
    * Create Virtual environment with __*'venv'*__ : `py -m venv .venv-trial`
        * Choose a specific Python version: `/c/Users/Ramakant/AppData/Local/Programs/Python/Python311/python -m venv .venv-Py311`
    * Actiavte virt. env:
        * Bash: `source .venv-trial/Scripts/activate`
        * Command Prompt: `.venv-trial\Scripts\activate.bat`
        * Power Shell: `.venv-trial\Scripts\Activate.ps1`
    * Deactivate: `deactivate`
* FastAPI
    * Run the server with 
        * `uvicorn car_sharing:app --reload`, OR
        * `fastapi dev car_sharing.py`

## Operational
* [Trainer Feedback](https://forms.gle/BfGFANkbAN9tSUZg9)
