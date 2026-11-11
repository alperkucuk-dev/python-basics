detections = ["car", "person", "car", "bicycle","person", "car", "truck", "person", "car" ]

def count_labels(labels):
    count = {}
    for i in labels:
        if i in count: 
            count[i] += 1
        else:
            count[i] =  1
    return count

        

counts = count_labels(detections)
print(counts)



def most_common(counts):
    common_label = None
    max_number = 0
    for i in counts:
        if counts[i] > max_number:
            max_number = counts[i]
            common_label = i
    return common_label, max_number

label,number = most_common(counts)

txt = f"Most common label is: {label}, count: {number}"
print(txt)