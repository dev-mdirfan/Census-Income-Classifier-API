'''
The above code will create REST API routers to our database models. Our models will be accessed by following the URL pattern:

`http://<server-ip>/api/v1/<object-name>`
You can notice that we include v1 in the API address. This might be needed later for API versioning.
'''

# backend/server/apps/endpoints/urls.py file
from django.urls import path
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from . import views

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView # import PredictView
# import ABTestViewSet and StopABTestView for A/B testing
from apps.endpoints.views import ABTestViewSet
from apps.endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")


urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    # add predict url
    re_path(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
    re_path(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", StopABTestView.as_view(), name="stop_ab"
    ),
    path("", views.home, name="home"),
]


"""
OK, let’s go into details. The PredictView accepts only POST requests. It is available at:


The `endpoint_name` is defining the endpoint that we are trying to reach. In our case (in local development) the ML algorithm can be accessed at:

```http://127.0.0.1:8000/api/v1/income_classifier/predict```

The `income_classifier` is the endpoint name (you can check endpoints at `http://127.0.0.1:8000/api/v1/endpoints`).

What is more, you can specify algorithm status or version in the URL. To specify status and version you need to include them in the URL, for example:

```http://127.0.0.1:8000/api/v1/income_classifier/predict?status=testing&version=1.1.1```.

By default, there is a used `production` status.

Based on endpoint name, status and version there is routing of the request to correct ML algorithm. If the algorithm is selected properly, the JSON request is forwarded to the algorithm object and prediction is computed.

In the code there is also included code that is drawing algorithm in case A/B testing, we will go into details of this code in the next chapter.

To check if is it working please go to `http://127.0.0.1:8000/api/v1/income_classifier/predict` and provide example JSON input:

```python
{
    "age": 37,
    "workclass": "Private",
    "fnlwgt": 34146,
    "education": "HS-grad",
    "education-num": 9,
    "marital-status": "Married-civ-spouse",
    "occupation": "Craft-repair",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 68,
    "native-country": "United-States"
}
```

The response contains probability, label, status and request_id. The request_id can be used later to provide feedback and ML algorithms monitoring.
"""