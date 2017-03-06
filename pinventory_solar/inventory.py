from pinventory_solar.predicates import (is_raw_raspberry, is_sol_raspberry)


def transform(inventory):
    """Transform an Ansible inventory object prior to JSON serialization.

    Creates three new groups called raw-raspberries, sol-raspberries
    and taken-raspberries. The first group contains all hosts which are
    called 'raspberrypi', the second group contains any Raspberry Pi devices
    which have hostnames beginning with 'sol-' and the third group contains
    any remaining Raspberry Pi devices.

    Args:
        inventory: A dictionary containing an Ansible inventory.
            The inventory contains per-host variables for 'ip_address',
            'hostname' and 'mac_address'.

    Returns:
        A dictionary containing an Ansible inventory.
    """
    all_raspberry_hosts = set(inventory['raspberries']['hosts'])
    raw_raspberry_hosts = set(host for host, hostvars in inventory['_meta']['hostvars'].items()
                              if is_raw_raspberry(hostvars))
    sol_raspberry_hosts = set(host for host, hostvars in inventory['_meta']['hostvars'].items()
                              if is_sol_raspberry(hostvars))
    taken_raspberry_hosts = all_raspberry_hosts - raw_raspberry_hosts - sol_raspberry_hosts
    inventory['raw-raspberries'] = {'hosts': sorted(raw_raspberry_hosts)}
    inventory['sol-raspberries'] = {'hosts': sorted(sol_raspberry_hosts)}
    inventory['taken-raspberries'] = {'hosts': sorted(taken_raspberry_hosts)}
    return inventory


