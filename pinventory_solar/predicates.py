def is_raw_raspberry(hostvars):
    return hostvars['hostname'].startswith('raspberrypi')


def is_sol_raspberry(hostvars):
    return hostvars['hostname'].startswith('sol-')

