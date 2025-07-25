import boto3

cloudwatch = boto3.client('cloudwatch')

# Create a CPU utilization alarm for an EC2 instance
response = cloudwatch.put_metric_alarm(
    AlarmName='HighCPUAlarm',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    EvaluationPeriods=1,
    Threshold=70.0,
    ComparisonOperator='GreaterThanThreshold',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-xxxxxxxxxxxxxxxxx'  # Replace with your EC2 instance ID
        },
    ],
    AlarmActions=[
        'arn:aws:sns:region:account-id:your-sns-topic'  # Replace with your SNS topic ARN
    ],
    Unit='Percent'
)

print("Alarm created successfully.")
