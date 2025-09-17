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
    * [Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)
        * [Advanced - HTTPS Redirect Middleware](https://fastapi.tiangolo.com/advanced/middleware/#httpsredirectmiddleware)
        * [Advanced - GZip Middleware](https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware)
    * [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
        * [Response Cookies](https://fastapi.tiangolo.com/advanced/response-cookies/)
    * [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
        * [Header: User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)
        * [Response Headers](https://fastapi.tiangolo.com/advanced/response-headers/)


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

## Contact
* ramakant.s.debata@gmail.com


---
---


# Instructions for Capstone Codebase Submission

## Repository Setup
* The capstone repository is `https://github.com/Training-Repository/20250903_Bosch_PyAdv_Capstone.git`.
* Clone the repository to your local machine:
  ```bash
  git clone <repo-link>
  ```

## Branch Creation and Code Submission
* Create a branch in your own name:
  ```bash
  git checkout -b your_firstname_lastname
  ```
  **Replace `your_firstname_lastname` with your actual name**

## Code Organization Requirements
* **Your branch must contain ONLY the `api_server/` folder at the top level**
* **The `data/` folder (with JSON files) must be inside `api_server/`**

**Example of correct structure:**
```
your_branch/
└── api_server/
    ├── main.py
    ├── models/
    ├── routes/
    ├── services/
    ├── utils/
    ├── data/
    │   ├── books.json
    │   ├── members.json
    │   └── transactions.json
    └── requirements.txt
```

**Incorrect structure (will cause evaluation issues):**
```
your_branch/
├── api_server/
├── data/          ❌ Wrong: data folder at top level
├── client_app/    ❌ Wrong: should not be included
└── other_files/   ❌ Wrong: no other folders allowed
```

* Copy your implemented code to the `api_server/` folder in the repository
* Add and commit your code:
  ```bash
  git add .
  git commit -m "Implement Library Management System API"
  ```

* Push your code to the repository, **specifying your branch explicitly**:
  ```bash
  git push origin your_firstname_lastname
  ```

## Important Submission Notes
* **Only the `api_server/` folder will be evaluated**
* **Do not modify** the `client_app/` folder or any evaluation scripts
* **Ensure your server starts** with: `uvicorn main:app --reload`
* **Test your implementation** using the provided client application before submitting

    