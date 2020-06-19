import os

class IDandPW():

    def __init__( self, name ):
        self.name = str( name )

    def store( self, userid, pw ):
        # Set environment variables
        os.environ[ self.name +  "ID" ] = userid
        os.environ[ self.name + "PW" ] = pw
    
    def get( self ):
        # Get environment variables
        userid = os.getenv( self.name +  "ID" )
        pw = os.environ.get( self.name + "PW" )
        return userid, pw

def main():
    alice_id_and_pw = IDandPW( "Alice" )
    alice_id_and_pw.store( "alice123", "password123" )
    print( alice_id_and_pw.get() )

if __name__ == "__main__":
    main()