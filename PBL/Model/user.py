import os

class User():

    def __init__( self, id=None, pw=None):
        self.userid = id
        self.userpw = pw

    def setUserInformation(self, id, pw):
        self.userid = id
        self.userpw = pw

        # Set environment variables
        os.environ[ "AMAZON_ID" ] = self.userid
        os.environ[ "AMAZON_PW" ] = self.pw
    
    def getUserInformation( self ):
        # Get environment variables
        self.userid = os.getenv( "AMAZON_ID" )
        self.pw = os.environ.get( "AMAZON_PW" )
        return (self.userid, self.pw)