import pytest
from constructs import Construct
from cdktf import Testing
from main import LambdaStack

class TestMain:

    def test_my_app(self):
        assert True

    def test_should_contain_lambda_function(self, tmp_path):
        app = Testing.app()
        stack = LambdaStack(app, "test")
        synth = Testing.synth(stack)

        assert synth.get_resource_count("aws_lambda_function") == 1
        assert synth.get_by_path("aws_lambda_function.lambda")["properties"]["function_name"] == "calculatrice"

    def test_should_use_python39_runtime(self, tmp_path):  
        app = Testing.app()
        stack = LambdaStack(app, "test")
        synth = Testing.synth(stack)

        assert synth.get_by_path("aws_lambda_function.lambda")["properties"]["runtime"] == "python3.9"

    def test_should_contain_input_queue(self, tmp_path):
        app = Testing.app()
        stack = LambdaStack(app, "test")
        synth = Testing.synth(stack)

        assert synth.get_resource_count("aws_sqs_queue") == 2
        assert synth.get_by_path("aws_sqs_queue.input_queue")["properties"]["name"] == "input_queue"

    def test_should_contain_output_queue(self, tmp_path):
        app = Testing.app()
        stack = LambdaStack(app, "test")
        synth = Testing.synth(stack)

        assert synth.get_resource_count("aws_sqs_queue") == 2
        assert synth.get_by_path("aws_sqs_queue.output_queue")["properties"]["name"] == "output_queue"

    def test_should_link_lambda_to_input_queue(self, tmp_path):
        app = Testing.app()
        stack = LambdaStack(app, "test")
        synth = Testing.synth(stack)

        assert synth.get_resource_count("aws_lambda_event_source_mapping") == 1
        assert synth.get_by_path("aws_lambda_event_source_mapping.event_source_mapping")["properties"]["event_source_arn"] == "${aws_sqs_queue.input_queue.arn}"
        assert synth.get_by_path("aws_lambda_event_source_mapping.event_source_mapping")["properties"]["function_name"] == "${aws_lambda_function.lambda.arn}"

    def test_should_set_environment_variable_for_output_queue(self, tmp_path):
        app = Testing.app()
        stack = LambdaStack(app, "test")
        synth = Testing.synth(stack)

        env_vars = synth.get_by_path("aws_lambda_function.lambda")["properties"]["environment"]["variables"]
        assert env_vars["OUTPUT_QUEUE_URL"] == "${aws_sqs_queue.output_queue.url}"