import requests
from colorama import Fore,init

init(autoreset=True)
url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
api_key = "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"
print(api_key)
def summarise(x):
    r = requests.post(url,headers = {'Authorization ':f"Bearer {api_key}"}, json= {'inputs':f'{x}'} )
    try:
        return r.json()[0]['summary_text']
    except:
        return 'Error occured'

print(Fore.YELLOW +"Welcome to text summarizer...")
name = input(Fore.CYAN +"Enter Your name:").strip().title()
text = input(Fore.GREEN+"Enter Your Text:".strip())
if not text:
    print(Fore.RED +("No text Entered! Please try again"))   

else:
    summary = summarise(text)
    print(Fore.GREEN+ f"Summary for {name}..")
    if summary:
        print(Fore.WHITE + summary)
    else:
        print(Fore.RED + "Failed to generate summary")
