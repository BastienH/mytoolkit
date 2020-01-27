def read(file):
    
    global data
    with open(file) as f:
        data = f.readlines()
    if type(data) is list:
        for d in data[:10]:
            print(d)
    elif type(data) is dict:
        keys = [k for k in data.keys()]
        print(f'Sample keys : {keys}')
