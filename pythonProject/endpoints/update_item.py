# import requests
# from requests.auth import HTTPBasicAuth
# from conftest import ApiCredentials
#
#
# class UpdateItem:
#     response = None
#     response_json = None
#
#     def update_item_summary(self, create_item):
#         credentials = ApiCredentials()
#         payload = {
#             "item": {
#                 "templateId": 452,
#                 "templateName": "Test API",
#                 "id": create_item,
#                 "summary": "Auto Created item Api 123",
#
#                 "status": "NEW",
#                 "fields": [
#                     {
#                         "id": 374,
#                         "name": "Text Area",
#                         "value": "Auto test 123456",
#                         "htmlValue": "Auto test 123456"
#                     }
#                 ],
#                 # "attributes": [
#                 #     {
#                 #         "id": 284,
#                 #         "name": "5D Level",
#                 #         "values": [
#                 #             {
#                 #                 "id": 1092,
#                 #                 "name": "Yes"
#                 #             }
#                 #         ]
#                 #     }
#                 # ],
#                 "authors": [
#                     {
#                         "id": 211,
#                         "username": "showroom",
#                         "firstName": "Showroom",
#                         "lastName": "Superuser",
#                         "email": "TEST2showroom@maik.com"
#                     }
#                 ],
#
#             },
#
#         }
#         self.response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
#                                      auth=HTTPBasicAuth(credentials.username, credentials.password),
#                                      json=payload).json()
#         print(self.response)
#         assert self.response['success'] is True
#         assert self.response['results'][0]['id'] == create_item
#         assert self.response['results'][0]['operation'] == 'UPDATE'
#         self.response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
#                                      auth=HTTPBasicAuth(credentials.username, credentials.password)).json()
#
#     def update_item_author(self, create_item):
#         credentials = ApiCredentials()
#         payload = {
#             "item": {
#                 "templateId": 452,
#                 "templateName": "Test API",
#                 "id": create_item,
#                 "summary": "Auto Created item Api",
#
#                 "status": "NEW",
#                 "fields": [
#                     {
#                         "id": 374,
#                         "name": "Text Area",
#                         "value": "Auto test 123456",
#                         "htmlValue": "Auto test 123456"
#                     }
#                 ],
#                 # "attributes": [
#                 #     {
#                 #         "id": 284,
#                 #         "name": "5D Level",
#                 #         "values": [
#                 #             {
#                 #                 "id": 1092,
#                 #                 "name": "Yes"
#                 #             }
#                 #         ]
#                 #     }
#                 # ],
#                 "authors": [
#                     {
#                         "id": 285,
#
#                     }
#                 ],
#
#             },
#
#         }
#         self.response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
#                                      auth=HTTPBasicAuth(credentials.username, credentials.password),
#                                      json=payload).json()
#         print(self.response)
#         assert self.response['success'] is True
#         assert self.response['results'][0]['id'] == create_item
#         assert self.response['results'][0]['operation'] == 'UPDATE'
#         self.response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
#                                      auth=HTTPBasicAuth(credentials.username, credentials.password)).json()
#
#     def update_item_status_active(self, create_item):
#         credentials = ApiCredentials()
#         payload = {
#             "item": {
#                 "templateId": 452,
#                 "templateName": "Test API",
#                 "id": create_item,
#                 "summary": "Auto Created item Api",
#
#                 "status": "ACTIVE",
#                 "fields": [
#                     {
#                         "id": 374,
#                         "name": "Text Area",
#                         "value": "Auto test 123456",
#                         "htmlValue": "Auto test 123456"
#                     }
#                 ],
#                 # "attributes": [
#                 #     {
#                 #         "id": 284,
#                 #         "name": "5D Level",
#                 #         "values": [
#                 #             {
#                 #                 "id": 1092,
#                 #                 "name": "Yes"
#                 #             }
#                 #         ]
#                 #     }
#                 # ],
#                 "authors": [
#                     {
#                         "id": 211,
#
#                     }
#                 ],
#                 "createDate": "2024-02-20T04:42:09.000+0000",
#                 "startDate": "2024-02-20T04:56:10.000+0000",
#                 "lastUpdateDate": "2024-02-20T04:56:17.000+0000",
#                 "likeCount": 0,
#                 "ackCount": 0,
#                 "voteCount": 0,
#
#             },
#
#         }
#
#         self.response = requests.put(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
#                                      auth=HTTPBasicAuth(credentials.username, credentials.password),
#                                      json=payload).json()
#         print(self.response)
#         assert self.response['success'] is True
#         assert self.response['results'][0]['id'] == create_item
#         assert self.response['results'][0]['operation'] == 'UPDATE'
#         self.response = requests.get(f"https://test2.kainexus.com/api/public/v1/json/item?id={create_item}",
#                                      auth=HTTPBasicAuth(credentials.username, credentials.password)).json()
#
#     def check_updated_summary(self):
#         expected_summary = "Auto Created item Api 123"
#         actual_summary = self.response['item']['summary']
#         assert actual_summary == expected_summary, f"Test FAILED: Summary mismatch. Expected: {expected_summary}, Actual: {actual_summary}"
#         print(f"Updated summary: {actual_summary}")
#
#     def check_updated_author(self):
#         expected_username = "AndreyTest123"
#         actual_username = self.response["item"]["authors"][0]["username"]
#         assert actual_username == expected_username, f"Test FAILED: Summary mismatch. Expected: {expected_username}, Actual: {actual_username}"
#         print(f"Updated Author: {actual_username}")
#
#     def check_updated_status_active(self):
#         expected_status = "ACTIVE"
#         actual_status = self.response['item']['status']
#         assert actual_status == expected_status, f"Test FAILED: Summary mismatch. Expected: {expected_status}, Actual: {actual_status}"
#         print(f"Updated Status: {actual_status}")
