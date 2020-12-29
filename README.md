# Modules
*This repository contains beneficial implemented modules.*
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
