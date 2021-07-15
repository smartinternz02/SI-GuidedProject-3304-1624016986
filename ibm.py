import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

authenticator = IAMAuthenticator('6b70mULMiqpFUewT7iTupesPv3uxzRDQKuUtV1JGBr4G')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/e9d708e4-adb9-4e77-903b-fb2c5b888e09')

response = natural_language_understanding.analyze(
    # url='www.ibm.com',
    text='''Networking is at the heart of the digital transformation. The network is essential to many business functions today, including business critical data and operations, cybersecurity, and so much more. A wide variety of career paths rely on the network -- so it's important to understand what the network can do, how it operates, and how to protect it.

This is a great course for developers, data scientists, cybersecurity specialists, and other professionals looking to broaden their networking domain knowledge. It’s also an excellent launching point for students pursuing a wide range of career pathways – from cybersecurity to software development to business and more. A Networking Academy digital badge is available for the instructor-led version of this course. No prerequisites required.''',
    features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False))).get_result()

print(json.dumps(response, indent=2))