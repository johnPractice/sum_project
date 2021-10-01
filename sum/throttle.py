from rest_framework.throttling import UserRateThrottle
from boomino.settings import USER_SUM_RATE


class SumThrottle(UserRateThrottle):
    rate = USER_SUM_RATE
