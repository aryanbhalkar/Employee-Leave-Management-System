import json
import boto3
import os
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")
s3 = boto3.client("s3")

TABLE_NAME = os.environ["TABLE_NAME"]
BUCKET_NAME = os.environ["BUCKET_NAME"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

table = dynamodb.Table(TABLE_NAME)

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,PUT,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }

def lambda_handler(event, context):
    try:
        method = event.get("httpMethod")
        path = event.get("path")

        if method == "POST" and path == "/leave/apply":
            return apply_leave(event)

        elif method == "GET" and path == "/leave/status":
            return get_leave_status(event)

        elif method == "PUT" and path == "/leave/update":
            return update_leave_status(event)

        else:
            return response(404, {"message": "Route not found"})

    except Exception as e:
        print("Error:", str(e))
        return response(500, {"error": str(e)})

def apply_leave(event):
    body = json.loads(event["body"])

    leave_id = str(uuid.uuid4())

    item = {
        "leaveId": leave_id,
        "employeeName": body["employeeName"],
        "employeeEmail": body["employeeEmail"],
        "leaveType": body["leaveType"],
        "startDate": body["startDate"],
        "endDate": body["endDate"],
        "reason": body["reason"],
        "status": "PENDING",
        "documentUrl": body.get("documentUrl", "Not uploaded"),
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="New Leave Request Submitted",
        Message=f"""
New leave request submitted.

Leave ID: {leave_id}
Employee: {item['employeeName']}
Email: {item['employeeEmail']}
Leave Type: {item['leaveType']}
Dates: {item['startDate']} to {item['endDate']}
Reason: {item['reason']}
Status: PENDING
"""
    )

    return response(201, {
        "message": "Leave request submitted successfully",
        "leaveId": leave_id,
        "status": "PENDING"
    })

def get_leave_status(event):
    params = event.get("queryStringParameters") or {}
    leave_id = params.get("leaveId")

    if not leave_id:
        return response(400, {"message": "leaveId is required"})

    result = table.get_item(Key={"leaveId": leave_id})

    if "Item" not in result:
        return response(404, {"message": "Leave request not found"})

    return response(200, result["Item"])

def update_leave_status(event):
    body = json.loads(event["body"])

    leave_id = body["leaveId"]
    new_status = body["status"]

    if new_status not in ["APPROVED", "REJECTED"]:
        return response(400, {"message": "Status must be APPROVED or REJECTED"})

    result = table.update_item(
        Key={"leaveId": leave_id},
        UpdateExpression="SET #status = :status",
        ExpressionAttributeNames={
            "#status": "status"
        },
        ExpressionAttributeValues={
            ":status": new_status
        },
        ReturnValues="ALL_NEW"
    )

    updated_item = result["Attributes"]

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"Leave Request {new_status}",
        Message=f"""
Leave request has been updated.

Leave ID: {leave_id}
Employee: {updated_item['employeeName']}
Status: {new_status}
"""
    )

    return response(200, {
        "message": "Leave status updated successfully",
        "leave": updated_item
    })
