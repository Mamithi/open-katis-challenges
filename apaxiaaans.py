name = list(input())

new_name = name[0]
let = name[0]

for i in range(1, len(name)):
    if name[i] != let:
        new_name += name[i]
        let = name[i]
        
print(new_name)