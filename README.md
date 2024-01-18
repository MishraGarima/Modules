# Modules
*This repository contains beneficial implemented modules.*
* Plots - I
  * This python code contains some simple sample plots using Matplotlib and Seaborn all with the purpose of fitting more than one piece of attribute information on single plot by adding dimensions to the plot and benefit comparison while maintaining easy readability of the plots.
  * First plot is heatmap with two different values placed one below the other in the call while color coded for the top value.
  * Second plot is simple bar plot with two line plots imposed on the same plot and values of line plots printed near the marker for bar plot axis on the left and line plot axis on the right.
  * Third plot is compound bar plot with three plots one value on left and other two values stacked one on the other on the right as part of single element on a particular x-axis value. 
* QuadraticEqnRoots_FastAPI
  * This file contains python code to find roots of a quadratic equation and provide result as json.
  * FastAPI GET call is used for the process.
  * Make a request to API call and obtain the quadratic equation root values as resultant json.
* Save ML Model
  * This file contains python code to save the trained ML model within as well as outside as seperate file and access it later in the code as per requirement.
* Scraping E-commerce Website
  * This file contains a function in python code to web scrape an E-commerce Website and store data in a CSV file.
  * It uses URL Library to open connection and download page and then closes the connection.
  * This page is parsed to html using Beautiful Soup object.
  * The data extracted (brand, product name, ...) is hence stored in a CSV file. This file is created at the same location where the python code file exists.  
* Scraping Wikipedia Page
  * The file contains a function in python code to web scrape a Wikipedia page.
  * It uses Requests library which sends get request to the desired url.
  * The page is then parsed to html text using Beautiful Soup object.
  * The desired part/division of the html page is kept aside and text is extracted and hence displayed.
* Send Mail with Image Attachment
  * This file contains a function in python code to send mail with an image attachment.
  * It uses MIME (Multipurpose Internet Mail Extensions) to form a structured mail with parts i.e. subject, main body, attachment using MIMEMultipart object. Attached text in main body and image using MIMEText and MIMEImage object.
  * A SMTP connection is established, logged in into desired sender account, the mail object created is send and the connection is closed. Here the sender email can be with any desired domain but needs low level security.
* Send Mail
  * The file contains a part of php code to send a mail.


### Implementation Instructions
* *QuadraticEqnRoots_FastAPI.py*
  * Save the .py file in python editor (e.g.: Pycharm)
  * Use command *> QuadraticEqnRoots_FastAPI:app --reload* on the terminal
  * Once you see 'Application startup complete' on the terminal go to browser (chrome) and execute:
    * Go to url *http://127.0.0.1:8000/docs* to open FastAPI Swagger and execute using UI
    * Use url *127.0.0.1:8000/?a=__&b=__&c=__* to obtain result where __ specify the desired value for variables a, b, and c (can be used directly as it is a GET request). E.g.: *127.0.0.1:8000/?a=1&b=-7&c=10*
  * Go to termial and press *Ctrl+C* to terminate the connection 
