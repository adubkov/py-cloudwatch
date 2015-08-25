# Cloudwatch module for Python

That module allow send metrics to cloudwatch.

## Install 
You can install py-cloudwatch with pip:
```
pip install py-cloudwatch
```

## Example

```python
cw = CloudWatch()

# Prepare metrics for cloudwatch
metric_request = CloudWatchMetric('jvm_gcutil_O', 55.3, 'AWS/EC2', {'AutoScalingGroupName': as_group}, unit='Percent')

# Put metric to cloudwatch
cw.put(metric_request)
```
