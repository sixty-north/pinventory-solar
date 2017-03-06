from pathlib import Path

from pinventory_solar.predicates import is_raw_raspberry, is_sol_raspberry


def transform(hostsvars):
    """Transform an Ansible hostsvars object prior to JSON serialization.

    Adds a host id variable for each host based on the last six digits
    its MAC address.

    Args:
        hostsvars: A dictionary mapping hosts (usually IP addresses) to
            dictionaries of variables for each host.

    Returns:
        A modified hostsvars dictionary.
    """
    for hostvars in hostsvars.values():
        hostvars['hostid'] = hostvars['mac'].replace(':', '')[6:]

        if is_raw_raspberry(hostvars):
            hostvars['ansible_user'] = 'pi'
            hostvars['ansible_ssh_pass'] = 'raspberry'

        if is_sol_raspberry(hostvars):
            hostvars['ansible_user'] = 'helios'
            hostvars['ansible_ssh_private_key_file'] = str(Path.home() / '.ssh' / 'helios_rsa')

    return hostsvars
