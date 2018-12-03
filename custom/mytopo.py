"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self)
	

        # Add hosts and switches
        hostOne = self.addHost( 'h1' )
        hostTwo = self.addHost( 'h2' )
	hostThree = self.addHost( 'h3' )
	hostFour  = self.addHost( 'h4' )
        leftSwitchUpper = self.addSwitch( 's1' )
	leftSwitchLower = self.addSwitch( 's2' )
	rightSwitchUpper = self.addSwitch( 's3' )
        rightSwitchLower = self.addSwitch( 's4' )

        # Add links
        self.addLink( hostOne, leftSwitchUpper )
        self.addLink( rightSwitchUpper, hostTwo  )
	self.addLink( hostThree, leftSwitchLower )
	self.addLink( rightSwitchLower, hostFour )
        self.addLink( leftSwitchUpper, rightSwitchUpper )
	self.addLink( leftSwitchLower, rightSwitchLower)
	self.addLink( leftSwitchUpper, leftSwitchLower)
	self.addLink( rightSwitchUpper, rightSwitchLower )

	
topos = { 'mytopo': ( lambda: MyTopo() ) }
