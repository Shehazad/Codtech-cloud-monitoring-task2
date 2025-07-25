# AWS CloudWatch Setup Instructions

## 1. Setup CloudWatch Dashboard
1. Login to AWS Console
2. Go to **CloudWatch** → **Dashboards**
3. Click **Create dashboard**
4. Enter name (e.g., `codtech-monitoring-dashboard`)
5. Add widgets like:
   - CPU Utilization
   - Network In/Out
   - Disk Read/Write

## 2. Create CloudWatch Alarms
1. Go to **CloudWatch → Alarms → Create Alarm**
2. Choose a metric (e.g., EC2 → Per-Instance Metrics → CPUUtilization)
3. Set threshold (e.g., > 70% for 5 minutes)
4. Configure actions (send email or SMS using SNS topic)
5. Name the alarm (e.g., `HighCPUAlarm`)

## 3. Test and Verify
- Trigger an alert by generating high CPU usage on EC2 instance
- Check email/SNS notification
- View live dashboard metrics

## 4. Optional: Use AWS CLI or Python (Boto3) to automate
- See `create_alarm.py` for example script
