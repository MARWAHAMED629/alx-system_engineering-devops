# 0x16. API advanced

## How to read API documentation to find the endpoints you’re looking for

API documentation typically includes details about available endpoints, their functionalities, required parameters, and expected responses. To find the endpoints you need:
- Start by reading the introduction or overview section of the documentation to understand the purpose of the API.
- Look for a section specifically dedicated to endpoints or methods. This should list all the available endpoints along with their descriptions.
- Pay attention to any authentication requirements or restrictions on certain endpoints.
- Read the descriptions of each endpoint to determine which one suits your needs.

## How to use an API with pagination

Pagination is commonly used in APIs to limit the number of results returned per request, making it more efficient to handle large datasets. To use pagination:
- Check the API documentation to see if pagination is supported and how it's implemented (e.g., query parameters like `page` and `limit`).
- Make an initial request to the API endpoint, specifying the desired pagination parameters.
- Process the results returned in the response.
- If there are more pages available, make subsequent requests by incrementing the page number or using a cursor provided by the API until you've retrieved all the data.

## How to parse JSON results from an API

JSON (JavaScript Object Notation) is a common format used for data interchange in APIs. To parse JSON results:
- Use built-in or third-party libraries depending on your programming language (e.g., `json` module in Python).
- Deserialize the JSON data received from the API response into native data structures (e.g., dictionaries, lists) that your programming language can work with.
- Access the parsed data elements using appropriate keys or indices.

## How to make a recursive API call

Recursive API calls are needed when an API's response contains nested or hierarchical data structures that you need to traverse to retrieve all the desired information. To make a recursive API call:
- Define a function that handles the API call and processing of the response.
- Within the function, make the initial API call.
- Process the response, and if it contains nested data structures, call the same function recursively with appropriate parameters to handle each nested level.
- Ensure there's a termination condition to prevent infinite recursion, typically based on the structure or size of the data being processed.

## How to sort a dictionary by value

Sorting a dictionary by value involves arranging its key-value pairs based on the associated values. To sort a dictionary by value:
- Use built-in functions or methods available in your programming language (e.g., `sorted()` in Python).
- Specify the sorting criterion, which in this case is the values of the dictionary.
- Apply the sorting function to the dictionary, which returns a sorted list of tuples containing key-value pairs.
- If needed, convert the sorted list back into a dictionary.
