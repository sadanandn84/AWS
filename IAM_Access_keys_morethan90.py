import boto3
from datetime import datetime

iam_client = boto3.client('iam')
accesskey_list = []
user_name_list = []

#marker = ''
#count = 0

list_iam_users = iam_client.list_users()                # boto wrapper API to list all IAM users
all_users = list_iam_users['Users']                     # This will check for User object in response syntax
truncation_check = list_iam_users['IsTruncated']        # This will check truncation status. why truncation value check required explained later in the code.

# This is a while loop, which will be active till truncation check value is True.
while truncation_check is True:                                 # 'IsTruncation = True - Means pagination is present i.e for eg. if 500 IAM users present, then the list records will be truncated may be for 200 user per page setting truncation flag 'True'.
    marker = list_iam_users['Marker']                           # If truncation is True, then there will marker value too, which will help in marking value for next page
    list_iam_users = iam_client.list_users(Marker=marker)       # This will add marker value and again will do List users function call to get next page value
    # The below for block will iterate through each users and retrieve user name and append it in a list for further transactions.
    for user in list_iam_users['Users']:
        user_name_list.append(user['UserName'])
    truncation_check = list_iam_users_with_marker['IsTruncated'] # This will again check whether 'IsTruncated' value is True or not.If True, then it won't exit while loop.

# If 'IsTruncated' is False, the below for loop will execute.
for user in list_iam_users['Users']:
    user_name_list.append(user['UserName'])

# The below code block will iterate over the appended list of usernames and provide those to list_access_keys function API
for name in user_name_list:
    list_access_keys = iam_client.list_access_keys(UserName=name)
    access_key_meta = list_access_keys['AccessKeyMetadata']         # This will retrieve the 'AccessKeyMetadata' object in response syntax
    # The below code block will iterate for items within 'AccessKeyMetadata', to retrieve created date and AccessKey Ids for the usernames.
    for item in access_key_meta:
        create_date = item['CreateDate']
        akwithouttz = create_date.replace(tzinfo=None)
        currentdate = datetime.utcnow()
        diff = currentdate - akwithouttz
        rotateperiod = diff.days
        if rotateperiod > 90:
            akid = item['AccessKeyId']
            print(akid)
            uname = name
            print(uname)
            #access_key_id_to_deactivate = item['AccessKeyId']
            #create_access_keys = iam_client.create_access_key(Username=name)
            #access_keyId = create_access_keys['AccessKey']['AccessKeyId']
            #secret_keyId = create_access_keys['AccessKey']['SecretAccesskey']
            #make_access_key_inactive = iam_client.update_access_key(AccessKeyId=)
            print ('Send 1st warning mail with Inactive key')
        else:
            print('deletion')




