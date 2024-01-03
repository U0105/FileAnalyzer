from ppadb.client import Client as AdbClient
def android_file(addres):
    clint = AdbClient(host='127.0.0.1',port=5037)
    devices = clint.devices()
    device = devices[0]
    return device.shell(f"cd {addres} && ls").strip().split()  