import requests
import aiohttp



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
        phone_number_id = '110679078718694'
        version = 'v17.0'
        
        url = 'https://graph.facebook.com' + f"/{version}/{phone_number_id}/messages"
        print('in non-asymc')
        headers = {
            'Authorization': 'Bearer EAANZBIgPmIpEBABCWZAGlws9A2Uoz9lGxIJHE6EEVmC7tpZBZAO1YR9x2nVZBiFZAZBgZBZALkUvEWSuPHtZAK1K194lTZBB87yqKZBnaNvutkqBkHdgN9EeZCdi9zGTCZA7EJHQz2WBvhDSQCBt3zzLUgR0G8stRtR5Kyu7sz1ZCycEnLDMQxZB2Ske37K3WLdZAgLFRkpVuoClP7MXu8AZDZD',
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
        
        response = requests.post(url, data=data, headers=headers)
        print(response)
        print('response stateus: ')
        print(response.status)  