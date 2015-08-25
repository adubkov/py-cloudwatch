import boto.utils
from boto.ec2 import cloudwatch

class CloudWatch(object):
    """ Interface to CloudWatch """
    def __init__(self):
        # Current host and region
        self.region = boto.utils.get_instance_metadata()['placement']['availability-zone'][:-1]
        self.instance_id = boto.utils.get_instance_metadata()['instance-id']

        # Connect to current host region using IAM credentials
        self.c = cloudwatch.connect_to_region(self.region)

    def put(self, metrics):
        """
        Put metrics to cloudwatch. Metric shoult be instance or list of
        instances of CloudWatchMetric
        """
        if type(metrics) == list:
            for metric in metrics:
                self.c.put_metric_data(**metric)
        else:
            self.c.put_metric_data(**metrics)

class CloudWatchMetric(object):
    """ Class of metric for CloudWatch class """
    def __init__(self, name, value, namespace, dimensions={}, unit='Count'):
        self.name = str(name)
        self.value = value
        self.namespace = str(namespace)
        self.dimensions = dimensions
        self.unit = str(unit)

    def __getitem__(self, key):
        # To get mapping **object work
        return self.__dict__.get(key)

    def keys(self):
        # To get mapping **object work
        return self.__dict__.keys()
