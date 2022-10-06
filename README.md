# my-aws

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_efs - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **HelloEfsFunction may not have authorization defined, Is this okay?**: Guided deployments will prompt to confirm when you have a publicly accessible API Gateway endpoint. If you do not want the endpoint to be publicly accessible without authorization, you can add `ApiFunctionAuth` settings to the `Api` event. [See the documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-apifunctionauth.html) for details.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
my-aws$ sam logs -n HelloEfsFunction --stack-name my-aws --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
my-aws$ pip install -r tests/requirements.txt --user
# unit test
my-aws$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
my-aws$ AWS_SAM_STACK_NAME=<stack-name> python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name my-aws
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)




https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html


https://towardsdatascience.com/how-to-build-a-serverless-application-using-aws-sam-b4d595fe689f


https://docs.amplify.aws/guides/functions/dynamodb-from-python-lambda/q/platform/js/#getting-an-item-by-primary-key-in-dynamodb-from-lambda


# Config new aws
aws configure --profile incloud-old
aws cloudformation delete-stack --stack-name cognito --profile arscloud-dev2

cat ~/.aws/credentials

# Run locally
sam local start-api --template=arscloud-lambdas-old.yaml 
--profile incloud-old


# sam local start-lambda
sam local start-lambda [OPTIONS]


# sam build & deploy
sam build
sam deploy --guided --template=aws_cfts/local-lambdas.yaml --profile incloud-old
--stack-name arscloud-lambdas --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset --region ap-northeast-1

sam build --template-file aws_cfts/dynamodb-tables.yaml --region ap-northeast-1 --profile incloud-old

sam deploy --template-file aws_cfts/dynamodb-tables.yaml --stack-name arscloud-table --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset --region ap-northeast-1 --profile incloud-old


# Connect boto3
Option 1:
import boto3
boto3.setup_default_session(profile_name = 'lico-dev')
dynamodb = boto3.resource('dynamodb')
u_table = dynamodb.Table('users')
u_table.put_item(Item={'username':'ars_admin', 'role': 'SUPER_ADMIN', 'email':'ars_admin@gmail.com'})
c_table = dynamodb.Table('companies')
c_table.put_item(Item={'companyId':'ars'})
d_table = dynamodb.Table('departments')
d_table.put_item(Item={'departmentId':'department', 'companyId':'ars', 'name':'Department'})
s_table = dynamodb.Table('stores')
s_table.put_item(Item={'companyId':'ars','departmentId':'department', 'storeId':'store', 'name':'store'})
d_table.put_item(Item={'deviceId':'BM003' ,'errorOccurrence':False,'lightingStatus':True, 'version':'store', 'connectionInformation':'info', 'latestUpdate':a})


Option 2:
session = boto3.session.Session(profile_name='arscloud-dev')
client = session.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')


# Create env
virtualenv -p python3.8 venv


# Layer
pip install -t _layers/python -r _layers/requirements.txt

aws lambda publish-layer-version \
    --layer-name layer-pandas-2 \
    --description "Layer pandas" \
    --zip-file fileb://_layers/layer.zip \
    --compatible-runtimes python3.8

zip -r _layers/layer.zip python    

https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path
https://medium.datadriveninvestor.com/how-to-set-up-layers-python-in-aws-lambda-functions-1355519c11ed
https://aws.plainenglish.io/creating-aws-lambda-layer-for-python-runtime-1d1bc6c5148d
https://towardsdatascience.com/building-custom-layers-on-aws-lambda-35d17bd9abbb


# Schedule
https://medium.com/thelorry-product-tech-data/building-a-simple-scheduled-task-with-aws-using-lambda-function-and-amazon-cloudwatch-event-e92e5e2418cf



## Install layer
```
pip3 install pyjwt -t _layers/python  
```

## Ref
### Cognito with boto3
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html
https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp


### Create template SES
```
aws ses list-templates --profile sqa
aws ses create-template --cli-input-json file://success_register.json --profile sqa
aws ses delete-template --profile sqa --template-name en_email_invite_register
```
https://medium.com/intelliconnect-engineering/send-emails-with-amazon-ses-part-1-simple-ses-template-1f400ac26c3f
https://docs.aws.amazon.com/cli/latest/reference/ses/index.html

### SES with boto3 
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html


### DynamoDB with boto3
https://highlandsolutions.com/blog/hands-on-examples-for-working-with-dynamodb-boto3-and-python

### Verify domain in SES
https://www.sendworks.com/support/sendx/amazon-ses-integration-guide


### Export api
aws apigateway get-export --stage-name api --parameters extensions='apigateway' --rest-api-id 6iulzc9uej --export-type swagger latestswagger2.json --profile arscloud-dev1

# Teminal
aws configure --profile arscloud-dev2
aws cloudformation delete-stack --stack-name lico-cognito --profile lico-dev

aws cognito-idp admin-update-user-attributes --user-pool-id ap-northeast-1_T33pNtfWO --username ars_admin --user-attributes Name="custom:role",Value="COMPANY_ADMIN" --profile incloud-old


aws cognito-idp admin-create-user --user-pool-id ap-northeast-1_FVcTUGjMn --username ars_admin --user-attributes Name="custom:companyId",Value="ars" --profile arscloud-dev2


aws cognito-idp admin-set-user-password --user-pool-id ap-northeast-1_FVcTUGjMn --username ars_admin --password 123456 --profile arscloud-dev2

aws cognito-idp admin-set-user-password \
  --user-pool-id ap-northeast-1_FVcTUGjMn  \
  --username ars_admin \
  --password 123456 \
  --permanent \
  --profile arscloud-dev2

aws cognito-idp list-users --user-pool-id ap-northeast-1_T33pNtfWO  --profile incloud-old


- sam package
  --template-file aws_cfts/user-management-endpoint.yaml
  --s3-bucket ${SAM_TEMPLATES_BUCKET}
  --output-template-file user-management-endpoint-packaged.yml
  --region ap-northeast-1
- sam deploy
  --template-file user-management-endpoint-packaged.yml
  --stack-name user-management-endpoint
  --s3-bucket ${SAM_TEMPLATES_BUCKET}
  --capabilities CAPABILITY_IAM
  --no-fail-on-empty-changeset
  --region ap-northeast-1
  --parameter-overrides "
  ParameterKey=CurrentServer,ParameterValue=${ENVIRONMENT}
  ParameterKey=AppClientID,ParameterValue=${APP_CLIENT_ID}
  ParameterKey=UserPoolID,ParameterValue=${USER_POOL_ID}
  ParameterKey=LayerVersion,ParameterValue=${LAYER_VERSION}
  ParameterKey=BMBackgroundBucket,ParameterValue=${BM_BG_BUCKET}
  ParameterKey=ProductionRoleARN,ParameterValue=${PROD_ROLE_ARN}
  ParameterKey=BinfileBucket,ParameterValue=${BINFILE_BUCKET}"