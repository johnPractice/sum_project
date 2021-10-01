
from django.urls import path
from django.conf.urls import url
from sum.views.history_view import HistoryView
from sum.views.sum_view import SumView
import re

from sum.views.total_view import TotalView
urlpatterns = [

    path('history/', HistoryView.as_view(), name="History of Sum's"),
    path('total/', TotalView.as_view(), name="Total of Sum's"),
    url(r'^', SumView.as_view(),),
]
