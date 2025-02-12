import http.client
import json
import ssl
import panel as pn

# Hardcoded API key
api_key = "5b899fe357msh7053521892e8476p18b54cjsn242e80188772"

def make_http_request(messages, temperature=0):
    try:
        context = ssl._create_unverified_context()
        conn = http.client.HTTPSConnection("open-ai21.p.rapidapi.com", context=context)
        
        payload = json.dumps({
            "messages": messages,
            "web_access": False,
            "system_prompt": "",
            "temperature": temperature,
            "top_k": 5,
            "top_p": 0.9,
            "max_tokens": 256
        })

        headers = {
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': "open-ai21.p.rapidapi.com",
            'Content-Type': "application/json"
        }

        conn.request("POST", "/conversationgpt35", payload, headers)
        res = conn.getresponse()
        data = res.read()
        
        if res.status != 200:
            print(f"Error: {res.status} {res.reason}")
            print(data.decode("utf-8"))
            return None
        
        return json.loads(data.decode("utf-8"))
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = make_http_request(messages)
    if response:
        return response['choices'][0]['message']['content']
    else:
        return "Error: Unable to get completion"

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = make_http_request(messages, temperature)
    if response:
        return response['choices'][0]['message']['content']
    else:
        return "Error: Unable to get completion"

# OrderBot
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600)))  # Removed style argument
 
    return pn.Column(*panels)

pn.extension()

panels = [] # collect display

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here...')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp, 
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300)
)

dashboard

messages =  context.copy()
messages.append(
{'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
)

response = get_completion_from_messages(messages, temperature=0)
print(response)