def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('hello', '123456789')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ipconfig('addr4'))
    
do_connect()


