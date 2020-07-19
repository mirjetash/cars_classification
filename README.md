# Car acceptability classification

A classfier to predict the acceptability of cars based on the cars' features such as buying price, maintenance price, number of doors, person capacity, luggage boot, safety. 

To build the classifier for this exercise, Support Vector Machines and Decision Trees are utilized.
The data that is used can be found in the *cars.csv* file.

The exercise_solution.ipynb file contains the python code with the explanations of the approach and the implementation of the classifiers. After going through this file you should refer to the *Using the Classifiers* section of this file to learn how to use the saved classifiers to make predictions.

### Prerequisites

To be able to run this project you need to install the requirements that are in the requirements.txt file, using the following command:

```
pip install requirements.txt
```

### Deploying the Classifers

To deploy the classifiers, I have utilized firefly, which is a lightweight python module for *function as a service*. 
The python file *model_api.py* loads the saved model and defines a function which wraps the call to the model's predict function, to make a prediction for a given input. 

Using firefly I have created an **API endpoint** that binds the predict function in the *model_api.py* file to the localhost port 5000.


### Using the Classifiers

To use the saved classifiers you can utilize the API endpoint created using firefly.

First in a terminal where the *model_api.py* file is, execute the command to bind the predict function the the port 5000 on localhost:

```
firefly model_api.predict --bind 127.0.0.1:5000
```

To make a prediction, on another command line you should execute the *curl* command to issue a POST request to the above created endpoint using the following command line:

```
curl -d '{"data": "dt vhigh vhigh 2 2 small low"}' http://127.0.0.1:5000/predict
```

The above command makes a prediction using the Decision Tree Classifier (**dt**), for the car with feature values **vhigh vhigh 2 2 small low**, for each of the features buying price, maintenance price, number of doors, person capacity, luggage boot, safety respectively.


The input for the prediction is provided with a dictionary having as follows:
{"data": "<classifier-to-use> <buying-price-feature> <maintenance-price-feature> <number-of-doors> <person-capacity> <luggage-boot> <safety> "}


Based on which classifier you want to use either SVM or Decision Tree set the <classifier-to-use> value to **svm** or **dt** respectively.

### Files on this directory

* README.md: this file you are reading.
* requirements.txt: file with the requirements that need to be installed.
* exercise_solution.ipynb:  Notebook file with the data analyses and implementation od the classifiers.
* cars.csv:  The dataset file.
* data_description.txt:  Description of the data features.
* model_api.py: Python code to implement the API endpoint.
* dt_model.sav: pre trained Decision Tree Classifier
* svm_model.sav: pre trained Support Vector Machine Classifier 

** dt_model.sav, and svm_model.sav are used by the model_api.py to make predictions



