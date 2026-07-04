import requests
api = "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"
url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
headers = {'Authorization' : f"Bearer {api}"}
topics = ['sports', 'technology', 'buisness', 'politics', 'health']

while True:
    headline = input("Enter Your headline of X for exit :")
    if(headline.lower() == 'x'):
        break
    payload = {
        'inputs' : headline,
        'parameters': {
            'candidate_labels':topics
        }
    }
    try:
        response = requests.post(url,headers=headers, json = payload)
        result = response.json()
        best = max(result, key = lambda x : x['score'])
        print("Headline", headline)
        print("Topic:", best['label'])
        print("Confidence:", round(best['score']*100, 2), "%")
    except Exception as e:
        print("Error :", e)
