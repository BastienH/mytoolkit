def dict_keys_to_variables(dict):
    for key, val in dict.items():
        if ' ' in key:
            key.split(' ')
            '_'.join(key)
            exec(key + f'= {val}')
            print(key, 'is now a variable')
     
    