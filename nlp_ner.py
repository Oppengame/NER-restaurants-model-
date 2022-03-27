import pandas as pd
file_name = 'tagged-data.bio'

def get_data(file_name):

    text = []
    data = []
    sample = []
    with open(file_name) as b:
        for line in b.readlines():
            if line == '\n':
                sample_dict = {}
                sample_dict['text'] = [s[1].strip() for s in sample]
                sample_dict['labels'] = [s[0] for s in sample]
                labels = []
                str_text = ''
                st = 0
                inside_lab = False
                for t,l in zip(sample_dict['text'], sample_dict['labels']):
                    print(t,l)

                    # label ended:
                    if l[0] != 'I' and inside_lab:
                        inside_lab = False
                        end = len(str_text)-1
                        labels.append([st, end, lab])

                    #label started:
                    if l[0] == 'B':
                        lab = l.split('-')[1]
                        st = len(str_text)
                        inside_lab = True

                    str_text += t + ' '
                    # labels.append(st,end,l)
                if inside_lab:
                    end = len(str_text) - 1
                    labels.append([st, end, lab])
                for l in labels:
                    print(str_text[l[0]:l[1]], l[2])
                data.append({"text": str_text, "labels": labels})
                sample = []
            else:
                line = line.split('\t')
                sample.append(line)
            # [text.append(li[2]) for li in line]
    return data

data = get_data(file_name)