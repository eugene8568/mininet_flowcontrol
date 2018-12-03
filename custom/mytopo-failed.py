"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.util import quietRun
from mininet.net  import Mininet
from mininet.link import TCLink
from mininet.cli  import CLI

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self, **opts ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self, **opts )

        # Add hosts and switches
        hostOne = self.addHost( 'h1' )
        hostTwo = self.addHost( 'h2' )
	hostThree = self.addHost( 'h3' )
	hostFour  = self.addHost( 'h4' )
        leftSwitchUpper = self.addSwitch( 's1' )
	leftSwitchLower = self.addSwitch( 's2' )
	rightSwitchUpper = self.addSwitch( 's3' )
        rightSwitchLower = self.addSwitch( 's4' )

	self.linkopts=linkopts

        # Add links
        self.addLink( hostOne, leftSwitchUpper ,**linkopts )
        self.addLink( leftSwitchUpper, rightSwitchUpper,**linkopts)
        self.addLink( rightSwitchUpper, hostTwo, **linkopts )
	self.addLink( hostThree, leftSwitchLower, **linkopts)
	self.addLink( leftSwitchLower, rightSwitchLower,**linkopts)
	self.addLink( rightSwitchLower, hostFour ,**linkopts)
	self.addLink( leftSwitchUpper, leftSwitchLower,**linkopts)
	self.addLink( rightSwitchUpper, rightSwitchLower,**linkopts )


    def runTopo():
	linkopts= dict(bw=10)
	topo=MyTopo(linkopts)
	net.Mininet(topo)
	net.start()
	
	# Enable sFlow
	quietRun('ovs-vsctl -- --id=@sflow create sflow agent=eth0 target=127.0.0.1 sampling=10 polling=20 -- -- set bridge s1 sflow=@sflow -- set bridge s2 sflow=@sflow -- set bridge s3 sflow=@sflow -- set bridge s4 sflow=@sflow')
	
if __name__=='__main__':
	runTopo()

topos = { 'mytopo': ( lambda: MyTopo() ) }
