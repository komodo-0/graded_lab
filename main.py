#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformAsset, AssetType
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.lambda_function import LambdaFunction
from cdktf_cdktf_provider_aws.lambda_event_source_mapping import LambdaEventSourceMapping
from cdktf_cdktf_provider_aws.data_aws_caller_identity import DataAwsCallerIdentity
from cdktf_cdktf_provider_aws.scheduler_schedule import SchedulerSchedule, SchedulerScheduleFlexibleTimeWindow, SchedulerScheduleTarget
from cdktf_cdktf_provider_aws.sqs_queue import SqsQueue


class LambdaStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        AwsProvider(self, "AWS", region="us-east-1")
        # Packagage du code
        code = TerraformAsset(
            self, "code",
            path="./lambda",
            type= AssetType.ARCHIVE
        )

        queue_output = SqsQueue(self,
                "queue_output",
                name="output_queue",
                visibility_timeout_seconds=60)

        # Create Lambda function
        lambda_function = LambdaFunction(self,
            "lambda",
            function_name="calculatrice",
            runtime="python3.9",
            memory_size=128,
            timeout=60,
            role="arn:aws:iam::515223095317:role/LabRole",
            filename= code.path,
            handler="lambda_function.lambda_handler",
            environment={"variables":{"foo":"bar", "OUTPUT_QUEUE_URL": queue_output.url}}
        )

        queue_input = SqsQueue(self,
                "queue_input",
                name="input_queue",
                visibility_timeout_seconds=60)
        
        LambdaEventSourceMapping(self,
        "event_source_mapping",
        event_source_arn=queue_input.arn,
        function_name=lambda_function.arn)


app = App()
LambdaStack(app, "graded_lab")
app.synth()
