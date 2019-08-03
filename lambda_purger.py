from __future__ import absolute_import, print_function, unicode_literals
import json
import boto3

def lambda_handler(event, context):
    purge_old_lambda_versions()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def convertIntoInteger(version):
  if version != '$LATEST':
    return int(version)
  else :
    return -99;


def findMaxVersion(versions):
  max_v = -99999;
  for version in versions:
    int_version = convertIntoInteger(version['Version']);
    if int_version > max_v :
      max_v = int_version;
  return max_v;


def purge_old_lambda_versions(marker = ''):
  version_to_retain = 4;
  client = boto3.client('lambda')
  if marker == '':
    functions = client.list_functions()
  else:
    functions = client.list_functions(Marker=marker)
  
  print('functions = {}: with marker = {}'.format(functions, marker))
  number_of_functions = 0;
  for function in functions['Functions']:
    number_of_functions+= 1
    versions = client.list_versions_by_function(FunctionName=function['FunctionArn'])['Versions']
    max_version = findMaxVersion(versions);
    
    print('max_version={} for function = {}'.format(max_version, function))
    
    if len(versions) == 1:
      print('{}: No purging is required'.format(function['FunctionName']))
      continue
    
    # print('function={})'.format(function))
    # print('versions={})'.format(versions))
    # print('function_version={})'.format(function['Version']))
    for version in versions:
      if version['Version'] != function['Version'] and (max_version - convertIntoInteger(version['Version'])) > version_to_retain:
        arn = version['FunctionArn']
        print('delete_function(FunctionName={})'.format(arn))
        client.delete_function(FunctionName=arn)
    print('{}: Purging is done'.format(function['FunctionName']))
  print('Number of functions : {}'.format(number_of_functions))
         
        

