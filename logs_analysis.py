""" 
You are given a stream of logging statements for a server as a list. Your 
product manager wants to know what categories of error are the most common, as well as what
 errors in the most common categories are the most common. 

Here are a few log lines, each is a string structured similarly to this:
[
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 Login Successful',
'[INFO] 200 User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]

Return a dictionary with logging statistics, that is formatted like so ( don't worry about 
spacing or formatting, only the data matters )
 
{
	'WARNING': {
		'403': {
			'Forbidden': {
				'No token in request parameters': 1
			}
		}
	},
	'ERROR': {
		'500': {
			'Server Error': {
				'int is not subscriptable': 2
			}
		}
	},
	'INFO': {
		'200': {
			'OK': {
				'Login Successful': 1,
				'User sent a message': 1
			}
		}
	}
}

When printed it will more likely look like this:
 
{'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}}, 'ERROR': {'500': {'Server Error': {'int is not subscriptable': 2}}}, 'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}}} """

def log_stats(logs):
    #master log list
    log_hashMap = {}

    #split each log into 2 parts: Log Header and Log Description
    for log in logs:
        log_parts = log.split(":")
        #splice out 1st white_space
        log_parts[1] = log_parts[1][1:]


        #Message Description is in log_parts[1]

        #log_header needs to be split again until its each individual part:
        #where at index 0: type of message, 1: status code, 2+ : message Title.
        log_header_parts = log_parts[0].split()

        message_title = ""

        #concatenate back message title:
        for index in range(2, len(log_header_parts)):
            if index == len(log_header_parts)-1:
                message_title += log_header_parts[index]
            else:
                message_title += log_header_parts[index] + " "
            
        
        log_header_parts[2] = message_title



        #remove the brackets in type of message:
        log_header_parts[0] = log_header_parts[0].replace("[", "").replace("]", "")

        # lets build the master hashMap:
        
        # lets begin by checking if the ley: 'type_of_message' exists in the master hashMap:
        if log_header_parts[0] not in log_hashMap:
            #then lets create it:
            log_hashMap[log_header_parts[0]] = {}
            log_hashMap[log_header_parts[0]][log_header_parts[1]] = {}
            log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]] = {}
            log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]][log_parts[1]] = 1
        else:
            # if it does exist, then we need to check the status code:
            if log_header_parts[1] not in log_hashMap[log_header_parts[0]]:
                log_hashMap[log_header_parts[0]][log_header_parts[1]] = {}
                log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]] = {}
                log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]][log_parts[1]] = 1
            else:
                #if now we need to check: message_title
                if log_header_parts[2] not in log_hashMap[log_header_parts[0]][log_header_parts[1]]:
                    log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]] = {}
                    log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]][log_parts[1]] = 1
                else:
                    # now we need to check for the message_description:
                    if log_parts[1] not in log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]]:
                        log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]][log_parts[1]] = 1
                    else:
                        log_hashMap[log_header_parts[0]][log_header_parts[1]][log_header_parts[2]][log_parts[1]] += 1
                    


                
    #finally, we return the entire  master dictionary.
    return log_hashMap


# test_data = [
# '[WARNING] 403 Forbidden: No token in request parameters',
# '[ERROR] 500 Server Error: int is not subscriptable',
# '[INFO] 200 OK: Login Successful',
# '[INFO] 200 OK: User sent a message',
# '[ERROR] 500 Server Error: int is not subscriptable'
# ]

    
# print(log_stats(test_data))