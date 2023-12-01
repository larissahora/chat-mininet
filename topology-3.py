from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI

class ExtendedTopo(Topo):
    def build(self):
        # adiciona os hosts e switches
        h1 = self.addHost('h1', ip='10.1.0.1/8')
        h2 = self.addHost('h2', ip='10.2.0.1/8')
        h3 = self.addHost('h3', ip='10.3.0.1/8')
        h4 = self.addHost('h4', ip='10.4.0.1/8')
        h5 = self.addHost('h5', ip='10.5.0.1/8')
        h6 = self.addHost('h6', ip='10.6.0.1/8')

        s1 = self.addSwitch('s1', cls=OVSSwitch)
        s2 = self.addSwitch('s2', cls=OVSSwitch)
        s3 = self.addSwitch('s3', cls=OVSSwitch)
        s4 = self.addSwitch('s4', cls=OVSSwitch)

        # adiciona os links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s4)
        self.addLink(h5, s4)
        self.addLink(h6, s4)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)


def configure_ovs_flows(net):
    net.get('s1').cmd('ovs-ofctl add-flow s1 in_port=1,actions=output:2,3,4,5')
    net.get('s1').cmd('ovs-ofctl add-flow s1 in_port=2,actions=output:1,3,4,5')
    net.get('s1').cmd('ovs-ofctl add-flow s1 in_port=3,actions=output:1,2,4,5')
    net.get('s1').cmd('ovs-ofctl add-flow s1 in_port=4,actions=output:1,2,3,5')
    net.get('s1').cmd('ovs-ofctl add-flow s1 in_port=5,actions=output:1,2,3,4')
    

    net.get('s4').cmd('ovs-ofctl add-flow s4 in_port=1,actions=output:2,3,4,5')
    net.get('s4').cmd('ovs-ofctl add-flow s4 in_port=2,actions=output:1,3,4,5')
    net.get('s4').cmd('ovs-ofctl add-flow s4 in_port=3,actions=output:1,2,4,5')
    net.get('s4').cmd('ovs-ofctl add-flow s4 in_port=5,actions=output:1,2,3,5')
   

if __name__ == '__main__':
    topo = ExtendedTopo()
    net = Mininet(topo=topo, switch=OVSSwitch)
    net.start()

    # Configure OVS flows
    configure_ovs_flows(net)

    # Start the command line interface
    CLI(net)

    # Stop the network
    net.stop()
