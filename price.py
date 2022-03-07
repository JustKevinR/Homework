def pricey_prod(d):
    
    
    sorted_list = sorted(d.items(), key=lambda x: x[1], reverse=True)

    result = []
    for x in sorted_list:
        if x[1] >= 500:
            result.append(x[0])
    return result
print(pricey_prod({"Computer" : 900, "TV" : 800, "Radio" : 50}))
