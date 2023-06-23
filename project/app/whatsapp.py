import requests
import aiohttp
import os



async def send_message(message):  
    print('whatsapp sendmessage triggered')
    print (message)
    version = 'v17.0'
    phone_number_id = '110679078718694'
    

    async with aiohttp.ClientSession() as session:
        url = 'https://graph.facebook.com' + f"/{version}/{phone_number_id}/messages"
        try:
          async with session.post(url, data=data, headers=headers) as response:
            if response.status == 200:
              print("Status:", response.status)
              print("Content-type:", response.headers['content-type'])

              html = await response.text()
              print("Body:", html)
            else:
              print(response.status)        
              print(response)        
        except aiohttp.ClientConnectorError as e:
          print('Connection Error', str(e))

    
    """ url = 'https://graph.facebook.com/v17.0/110679078718694/messages' """
def non_async_send(message):
        print('in non-asymc')
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
        
        print(response)

         