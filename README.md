<p align="center">
<img src="https://i.imgur.com/S7DkZtr.png" width="250" alt="People Data Labs Logo">
</p>
<h1 align="center">People Data Labs Python Library</h1>
<p align="center">
A tiny, universal Python client for the People Data Labs API.
</p>

#
This is a simple Python client library to access the various API endpoints provided by [People Data Labs](https://www.peopledatalabs.com/).

This library bundles up PDL API requests into simple function calls, making it easy to integrate into your projects. You can use the various [API endpoints](#endpoints) to access up-to-date, real-world data from our massive [Person](https://docs.peopledatalabs.com/docs/stats) and [Company](https://docs.peopledatalabs.com/docs/company-stats) Datasets.  

## ✨ Features
- Tiny <2KB size gzip
- Supports all People Data Labs API endpoints

## Table of Contents
- [🔧 Installation](#installation)
- [🚀 Usage](#usage)
- [🌐 Endpoints](#endpoints)
- [📘 Documentation](#documentation)
    - [Special Note about Search API Support](#special-note)


## 🔧 Installation <a name="installation"></a>

1. Pull the package from the npm repository:

```bash
pip install pypdl
```

2. Sign up for a [free PDL API key](https://www.peopledatalabs.com/signup)

## 🚀 Usage <a name="usage"></a>

First, create the PyPDL client:

```py
from pypdl import PyPDL

pdl = PyPDL({'api_key': 'YOUR API KEY'})
```

Then, send requests to any PDL API Endpoint:

**Getting Person Data**
```py
# By Enrichment
data = pdl.person().enrichment({ 'phone': '4155688415' })
print(data)
```

## 🌐 Endpoints <a name="endpoints"></a>

**Person Endpoints**
| API Endpoint | PyPDL Function |
|-|-|
| [Person Enrichment API](https://docs.peopledatalabs.com/docs/enrichment-api) | `PyPDL.person().enrichment(...params)` |
| [Person Search API](https://docs.peopledatalabs.com/docs/search-api) | SQL: `PyPDL.person().search.sql(...params)` <br/> Elasticsearch: `PyPDL.person().search.elastic(...params)`|
| [Person Retrieve API](https://docs.peopledatalabs.com/docs/person-retrieve-api) | `PyPDL.person().retrieve(...params)` |
| [Person Identify API](https://docs.peopledatalabs.com/docs/identify-api) | `PyPDL.person().identify(...params)` |

**Company Endpoints**
| API Endpoint | PyPDL Function |
|-|-|
| [Company Enrichment API](https://docs.peopledatalabs.com/docs/company-enrichment-api) | `PyPDL.person().enrichment(...params)` |
| [Company Search API](https://docs.peopledatalabs.com/docs/company-search-api) | SQL: `PyPDL.person().search.sql(...params)` <br/> Elasticsearch: `PyPDL.person().search.elastic(...params)`|

**Supporting Endpoints**
| API Endpoint | PyPDL Function |
|-|-|
| [Autocomplete API](https://docs.peopledatalabs.com/docs/autocomplete-api) | `PyPDL.autocomplete(...params)` |
| [Company Cleaner API](https://docs.peopledatalabs.com/docs/cleaner-apis#companyclean) | `PyPDL.company().cleaner(...params)` |
| [Location Cleaner API](https://docs.peopledatalabs.com/docs/cleaner-apis#locationclean) | `PyPDL.location().cleaner(...params)` |
| [School Cleaner API](https://docs.peopledatalabs.com/docs/cleaner-apis#schoolclean) | `PyPDL.school().cleaner(...params)` |


## 📘 Documentation <a name="documentation"></a>

All of our API endpoints are documented at: https://docs.peopledatalabs.com/

These docs describe the supported input parameters, output responses and also provide additional technical context.

As illustrated in the [Endpoints](#endpoints) section above, each of our API endpoints is mapped to a specific method in the PyPDL class.  For each of these class methods, **all function inputs are mapped as input parameters to the respective API endpoint**, meaning that you can use the API documentation linked above to determine the input parameters for each endpoint.

As an example:

The following is **valid** because `name` is a [supported input parameter to the Person Identify API](https://docs.peopledatalabs.com/docs/identify-api-reference#input-parameters):
```py
PyPDL.person().identify({ 'name': 'sean thorne' })
```

Conversely, this would be **invalid** because `fake_parameter` is not an input parameter to the Person Identify API:
```py
PyPDL.person().identify({ 'fake_parameter': 'anything' })
```


#### Special Note about Search API Support <a name="special-note"></a>

Our Person Search API and Company Search API endpoints both support two types of query syntax: you can construct search queries using either `SQL` or `Elasticsearch` syntax.

In the PyPDL class, the person and company search functions are broken out into two syntax-specific methods as follows:
| Data Type | Search Query Syntax | Function |
| -- | -- | -- |
| Person | SQL | `PyPDL.person().search.sql(...params)` |
| Person | Elasticsearch | `PyPDL.person().search.elastic(...params)` |
| Company | SQL | `PyPDL.company().search.sql(...params)` |
| Company | Elasticsearch | `PyPDL.company().search.elastic(...params)` |

You can pass your query to these methods using the special `search_query` function argument, as shown in the following example:

```py
sql_query = "SELECT * FROM company WHERE website='peopledatalabs.com';"

data = PyPDL.company().search.sql({ 'sql_query': 'sqlQuery', 'size': 10 })
print(data)
```