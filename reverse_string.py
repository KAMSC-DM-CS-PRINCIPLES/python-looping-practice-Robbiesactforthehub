def reverse_string(text):
    esrever=[]
    for i in range(len(text)):
        esrever.append(text[len(text)-i-1])
    return "".join(esrever)