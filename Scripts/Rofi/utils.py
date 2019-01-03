from subprocess import check_output

def subtext(s):
    return f' <span weight="light"><i><small>({s})</small></i></span>'

def rofi(items, *args, p='', **kwargs):
    command = ['rofi', '-dmenu', '-i', '-p', p]
    if items:
        if isinstance(items, list):
            items = '\n'.join(items)
        items = items.encode()
    else:
        items = b''
        command += ['-l', '-1']
    command += args
    for k, v in kwargs.items():
        command += ['-' + k, v]
    try:
        output = check_output(command, input=items)
        try:
            return int(output)
        except:
            return output.decode()
    except CalledProcessError:
        return None
