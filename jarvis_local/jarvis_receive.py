from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

###################################################################################################################################### 
pnconfig = PNConfiguration()
 
pnconfig.subscribe_key = 'sub-c-56f8fe2a-0dcd-11e7-83b6-0619f8945a4f'
pnconfig.publish_key = 'pub-c-b432bbef-d96b-4a40-91d4-7ae1c6d96ee6'
 
pubnub = PubNub(pnconfig)


def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        print "Published"
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
 
 
class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
 
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            # pubnub.publish().channel("redChannel").message("hello!!").async(my_publish_callback)
            pass
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
 
    def message(self, pubnub, message):
        print "This is what I received from the server side", message.message
        msg = " Custom message based on intent under construction"
        pubnub.publish().channel('blueChannel').message(msg).async(my_publish_callback)
        pass  # Handle new message stored in message.message

  
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('redChannel').execute()



##################################################################################################################################