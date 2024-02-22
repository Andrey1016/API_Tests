# import requests
# from requests.auth import HTTPBasicAuth
# import json

#
#
# def api_request_with_basic_auth(username, password):
#     api_url = 'https://test2.kainexus.com/api/public/v1/json/itemList?offset=22&id=4829'
#
#     response = requests.get(api_url, auth=HTTPBasicAuth(username, password))
#     # items = api_url('items', [])
#     authors = response.json()
#     # assert isinstance(authors, list)
#     print(authors)
#
#     # assert len(autors)
#     # assert autors[0][]
#
# #     response_json = json.loads(response_text)
# #
# #     expected_count = 23
# #     expected_total_count = 23
# #     expected_offset = 0
# #     expected_limit = 30000
# #
# #     assert response_json[
# #                "count"] == expected_count, f"Expected count: {expected_count}, Actual count: {response_json['count']}"
# #     assert response_json[
# #                "totalCount"] == expected_total_count, f"Expected totalCount: {expected_total_count}, Actual totalCount: {response_json['totalCount']}"
# #     assert response_json[
# #                "offset"] == expected_offset, f"Expected offset: {expected_offset}, Actual offset: {response_json['offset']}"
# #     assert response_json[
# #                "limit"] == expected_limit, f"Expected limit: {expected_limit}, Actual limit: {response_json['limit']}"
# #
# #
# # response_text = '{"count":23,"totalCount":23,"offset":0,"limit":30000}'
#
# if __name__ == "__main__":
#     api_username = 'api'
#     api_password = 'MjczLTVhYjZiYTFmLTYyNmItNDQxMS1iNjExLTYwY2M2Mzk4ZTc5Ng=='
#     api_request_with_basic_auth(api_username, api_password)



