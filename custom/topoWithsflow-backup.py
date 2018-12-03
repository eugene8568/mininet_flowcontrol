#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net  import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli  import CLI
from mininet.util import quietRun

class MyTopo( Topo ):

    def __init__( self , **opts):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self, **opts )


	#c = RemoteController('c',ip='127.0.0.1',port=6653)
	#self = Mininet(link=TCLink);

	# set link speeds to 10Mbit/s
	linkopts = dict(bw=10)


# Add hosts and switches
	host1  = self.addHost('h1',ip='10.0.0.1',mac='00:04:00:00:00:01')
	host2  = self.addHost('h2',ip='10.0.0.2',mac='00:04:00:00:00:02')
	host3 = self.addHost('h3',ip='10.0.0.3',mac='00:04:00:00:00:03')
	host4 = self.addHost('h4',ip='10.0.0.4',mac='00:04:00:00:00:04')

	leftSwitchUpper     = self.addSwitch('s1')
	leftSwitchLower   = self.addSwitch('s2')
	rightSwitchUpper  = self.addSwitch('s3')
	rightSwitchLower = self.addSwitch('s4')

# Add links

	self.addLink(host1,  leftSwitchUpper,    **linkopts )
	self.addLink(leftSwitchUpper, rightSwitchUpper, **linkopts )
	self.addLink(rightSwitchUpper, host2 ,   **linkopts )
	self.addLink(host3, leftSwitchLower , **linkopts )
	self.addLink(leftSwitchLower, rightSwitchLower,   **linkopts )

	self.addLink(rightSwitchLower, host4,**linkopts )
	self.addLink(leftSwitchUpper,leftSwitchLower, **linkopts )
	self.addLink(rightSwitchUpper,rightSwitchLower,**linkopts )

#topos = { 'mytopo': ( lambda: MyTopo() ) }

def Run():
	topo= MyTopo()


	# Start
	#net.controllers = [ c ]
	c = RemoteController('c',ip='127.0.0.1',port=6653)
	net = Mininet(topo=topo, link=TCLink, controller=None )
	net.addController(c)
	net.start()
	CLI(net)

	# Enable sFlow
	quietRun('ovs-vsctl -- --id=@sflow create sflow agent=eth0 target=\"127.0.0.1:6343\" sampling=10 polling=20 -- -- set bridge s1 sflow=@sflow -- set bridge s2 sflow=@sflow -- set bridge s3 sflow=@sflow -- set bridge s4 sflow=@sflow')

	# Clean up
	net.stop()

if __name__=='__main__':
	Run()

