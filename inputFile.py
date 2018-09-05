result = [l for l in open("input.file") if l.startswith("error: ")]
result = list(filter(lambda l : l.startswith("error: "), open("input.file").readlines()))

result = []
for l in open("input.file").read().split("\n") :
    if l.startswith("error: ") :
       result.append(l)

result = []
for l in open("input.file", "w+").read() :
    if l.startswith("error: ") :
       result.append(l)
print(result)