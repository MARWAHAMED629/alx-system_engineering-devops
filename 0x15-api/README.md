# 0x15. API

## Description
The aim of this project is to write automated tasks in Python instead of Bash.
Those tasks focus on getting data from an API and exporting it in JSON or CSV format.

(https://github.com/MARWAHAMED629/alx-system_engineering-devops/assets/59849322/85b76674-5a61-4499-bd40-4e333d124764)

## What is an API?
Application Programming Interface (API) is a software interface that allows two applications to 
interact with each other without any user intervention. API is a collection of software functions and procedures. 
In simple terms, API means a software code that can be accessed or executed. 
API is defined as a code that helps two different software’s to communicate and exchange data with each other.
------------------
## How does api work?
To understand the functionality of the API, let see the following example:

API Example 1:

Let see how API works using simple daily life example. 
Imagine that you went to a restaurant to take lunch or dinner. The waiter comes to you gives you a menu card, 
and you will provide personalize it order like you want a veg sandwich but without onion.
After some time, you will get your order from the waiter. However, it is not that simple as it looks as there is some process that happens in between.
Here, the waiter plays an important part as you will neither go to the kitchen to collect your 
order nor will you tell the kitchen staff what you want all this done by the waiter.
-------------
API Example 2:

After understanding the concept, let us take some more technical examples.

For example, you go to the movie site, you enter your movie, name, and credit card information, and behold, you print out tickets.

They are collaborating with other applications. This integration is called “seamless,” 
as you never have a clue when a software role is passed from one application to another.


## Why would we need an API?
Here, are some reason for using API:

Application Programming Interface acronym API helps two different software’s to communicate and exchange data with each other.
It helps you to embed content from any site or application more efficiently.
APIs can access app components. The delivery of services and information is more flexible.
Content generated can be published automatically.
It allows the user or a company to customize the content and services which they use the most.
Software needs to change over time, and APIs help to anticipate changes.
Features of API
Here are some important features of API:

It offers a valuable service (data, function, audience,.).
It helps you to plan a business model.
Simple, flexible, quickly adopted.
Managed and measured.
Offers great developer support.

## Types of API:-
There are mainly four main types of APIs:

Open APIs: These types of APIs are publicly available to use like OAuth APIs from Google. 
It has also not given any restriction to use them. So, they are also known as Public APIs.
Partner APIs: Specific rights or licenses to access this type of API because they are not available to the public.
Internal APIs: Internal or private. These APIs are developed by companies to use in their internal systems. 
It helps you to enhance the productivity of your teams.
Composite APIs: This type of API combines different data and service APIs.

## Table of contents
Files | Description
----- | -----------
[0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py) | Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress
[1-export_to_CSV.py](./1-export_to_CSV.py) | Python script to export data in the CSV format, extending from 0-gather_data_from_an_API.py
[2-export_to_JSON.py](./2-export_to_JSON.py) | Python script to export data in the JSON format, extending from 0-gather_data_from_an_API.py
[3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py) | Python script to export data in the JSON format, extending from 0-gather_data_from_an_API.py and 2-export_to_JSON.py 
