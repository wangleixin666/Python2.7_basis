list_loss = []

for i in range(1, 5, 5):
    list_loss.append(i)

# print type(list_loss)
print list_loss

summary = 0

for j in range(len(list_loss)):
    summary += int(list_loss[j])

print summary / len(list_loss)
