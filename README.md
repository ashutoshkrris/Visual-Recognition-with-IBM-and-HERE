# Visual Recoginition with IBM Watson and HERE Location Services

This is an application to find restaurants with the help of food image we have. It uses **IBM Watson** for **Visual Recognition** and **HERE location services** for **maps and location analytics**.

## Prerequisites

To start with Image Recognition, you will need:

* An IBM Cloud account (you can sign up [here](https://cloud.ibm.com/registration)) 
* Python 3.8  and pip
* [Freemium](https://developer.here.com/sign-up?utm_medium=referral&utm_source=IBM_DevBlog&create=Freemium-Basic&keepState=true&step=account) account on HERE Developer portal

From IBM Cloud, you need to access Watson and create a Visual Recognition service. From the created service, you have to acquire the API key for performing operations through the API.

You will also need an API key from the HERE Developer Portal (which is used in the code). Simply sign up for your free account and generate API key on your account page.

## Installations

Install Watson Developer Cloud using pip:
* `pip install --upgrade "ibm-watson>=4.0.1"`

Install Flask using pip:
* `pip install flask`


**Note** : Don't forget to put all the APIs in the [config.py](https://github.com/ashutoshkrris/Visual-Recognition-with-IBM-and-HERE/blob/master/config.py) file.


Feel free to fork the file and clone it for your use cases.
