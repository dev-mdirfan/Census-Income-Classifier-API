# ML With Django

- In this project we are going to use Django to create a web application that will use machine learning to predict the price of a house based on the features of the house.
- This project is a simple Django project that uses DRF to create an API for a ML model. The model is trained on the Adult Income data set and predicts whether income exceeds $50K/year based on census data.

In this tutorial, I will use [Adult Income data set](https://archive.ics.uci.edu/dataset/2/adult) or [adult DataSet](adult.zip). In this data set, the ML will be used to predict whether income exceeds $50K/year based on census data. I will load data from my [public repository with data sets good for start with ML](https://github.com/pplonski/datasets-for-start).

- for jupyter notebook dataset that are online: [online data set](https://raw.githubusercontent.com/plotly/datasets/master/adult_income.csv) please load not download.

## Concepts

The `numpy` and `pandas` packages are used for data manipulation. The `joblib` is used for ML objects saving. Whereas, the `sklearn` package offers a wide range of ML algorithms. We need to reload Jupyter after installation.

- build Django models to store information about ML algorithms and requests in the database,
- write REST API for your ML algorithms with the Django REST Framework.

### How to use Jupyter Notebook in Django

**Install Jupyter Notebook:**
```bash
pip install jupyter notebook
```

**Use local venv:**
```bash
ipython kernel install --user --name=venv
```

### Working with models

We defined three models:

- Endpoint - to keep information about our endpoints,
- MLAlgorithm - to keep information about ML algorithms used in the service,
- MLAlgorithmStatus - to keep information about ML algorithm statuses. The status can change in time, for example, we can set testing as initial status and then after testing period switch to production state.
- MLRequest - to keep information about all requests to ML algorithms. It will be needed to monitor ML algorithms and run A/B tests.

### Create REST API for models

So far we have defined database models, but we will not see anything new when running the web server. We need to specify REST API to our objects. The simplest and cleanest way to achieve this is to use Django REST Framework (DRF). To install DRF we need to run:

```bash
pip install djangorestframework markdown django-filter
```

**To see something in the browser we need to define:**
- serializers - they will define how database objects are mapped in requests,
- views - how our models are accessed in REST API,
- urls - definition of REST API URL addresses for our models.

we have created two ML algorithms (with Random Forest and Extra Trees). They were implemented in the Jupyter notebook.

Now, we will write code on the server-side that will use previously trained algorithms. In this chapter we will include on server-side only the Random Forest algorithm (for simplicity).

We have our ML algorithm in the database and we can access information about it with REST API, but how to do predictions?



## Installation

- Clone the repository
- Create a virtual environment
- Install the requirements
- Run the server

```bash
git clone 
cd 
python3 -m venv venv

source venv/bin/activate
pip install -r requirements.txt

python manage.py runserver
```

**To build docker images please run:**

```bash
docker-compose build
```

**To start the docker images please run:**

```bash
docker-compose up
```

**You should be able to see the running server at the address:** http://0.0.0.0:8000/api/v1/

open http://127.0.0.1:8000/api/v1/ in the web browser. You should see DRF view. The DRF provides nice interface, so you can click on any URL and check the objects (for example on http://127.0.0.1:8000/api/v1/endpoints).

you can check the endpoints and ML algorithms in the browser.

At the URL: http://127.0.0.1:8000/api/v1/endpoints you can check endpoints :- List of endpoints defined in the service

 and at http://127.0.0.1:8000/api/v1/mlalgorithms you can check algorithms :- List of ML algorithms defined in the service


## References

- Documentation Tutorial: https://www.deploymachinelearning.com/
