from protorpc import messages

class AccountSetupRequest(messages.Message):
    """ProtoRPC message definition to represent a new user query""" 
    #TODO: Add user authentication
    username = messages.StringField(1)
    email = messages.StringField(2)

class BlankResponse(messages.Message):
    """ Blank message response"""

