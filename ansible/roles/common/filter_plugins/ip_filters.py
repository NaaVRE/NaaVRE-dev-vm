import ipaddress


def ip(value):
    """Return the IP address from a CIDR-notation interface string.

    Example: '192.168.1.5/24' -> '192.168.1.5'
    """
    interface = ipaddress.IPv4Interface(value)
    return str(interface.ip)


def network_address(value):
    """Return the network address from a CIDR-notation interface string.

    Example: '192.168.1.5/24' -> '192.168.1.0'
    """
    interface = ipaddress.IPv4Interface(value)
    return str(interface.network.network_address)


def network_prefixlen(value):
    """Return the prefix length from a CIDR-notation interface string.

    Example: '192.168.1.5/24' -> '24'
    """
    interface = ipaddress.IPv4Interface(value)
    return str(interface.network.prefixlen)


class FilterModule(object):
    def filters(self):
        return {
            "ip": ip,
            "network_address": network_address,
            "network_prefixlen": network_prefixlen,
            }
