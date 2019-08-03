# LambdaPurger
Script to parse all the AWS lambdas and purge all  Lambda's older versions

## How to Use this script?
The default behavior of this lambda is that it will clean all the old versions except latest 5 versions. You can change this by changing version_to_retain variable in purge_old_lambda_versions method.

 - Create the lambda using the python script. Use Python version 3.7
 - Create a Role to execute the lambda
 - Use the policy.json as the policy for this role
 - Use any payload. Sample ``` {"key1":"value1","key2":"value2","key3":"value3"}```
 - The lambda will return ``` {"statusCode":200,"body":"\"Hello from Lambda!\""} ```
 
## Small Trick
If you don't have space even to create this lambda then go to any lambda detail page and click "Qualifier" and click version and select oldest version. Then click "Action" and "Delete Function".
Voila!! 
Now create the purger lambda and execute it. 