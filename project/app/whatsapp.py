import requests
import os



def non_async_send(message):
        bearer = os.environ['WHATSAPP_BEARER']
        phone_number_id = '110679078718694'
        version = 'v17.0'
        url = 'https://graph.facebook.com' + f"/{version}/{phone_number_id}/messages"
        url = "https://graph.facebook.com/v17.0/110679078718694/messages"
        headers = {
            'Authorization': 'Bearer ' + bearer,
            'Content-Type': 'application/json'
        }
        data = {
            'messaging_product': 'whatsapp',
            'recipient_type': "individual",
            'to': '27799140837',
            'type': 'text',
            'text': {
                   'body': message
                    }
       }
        
        
        response = requests.post(url, headers=headers, json=data)
        
        print("response from whatsapp send")
        print(response)

         