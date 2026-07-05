import requests
HFAPIKEY = "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"
API = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {
    "Authorization": f"Bearer {HFAPIKEY}"
} 
while True:
    s1 = input("\nStatement 1:")
    if s1.lower() == "exit":
        break
    s2 = input("Statemenr 2")
    if s2.lower() == "exit":
        break

    payload = {
        "inputs": {
            "source_sentence": s1,
            "sentences": [s2]
        }
    }

    r = requests.post(API, headers=headers, json=payload)

    if r.ok:
        score = r.json()[0]
        print(f"Similarity : {score:.2%}")

        if score >= 0.72:
            print("DUPLICATE")
        else:
            print("DIFFERENT")
    else:
        print("ERROR:", r.text)
