file_name = 'tagged-data.bio'
sample = []

with open(file_name) as b:
    for line in b.readlines():
        if line != '\n':
            sample.append(line.split('\t'))
        else:
            sample_dict = {}
            sample_dict['text'] = [s[1].strip() for s in sample]
            sample_dict['labels'] = [s[0].strip() for s in sample]
            labels = []
            st = 0
            str_text =''
            inside_label = False
            for t,l in zip(sample_dict['text'], sample_dict['labels']):

                if l[0] != 'I' and inside_label:
                    inside_label = False
                    end = len(str_text) - 1
                    labels.append([st, end, lab])

                if l[0] == 'B':
                    lab = l.split('-')[1]
                    st = len(str_text)
                    inside_label = True

                str_text += t + ' '

                if inside_label:
                    end = len(str_text) - 1
                    labels.append([st, end, lab])

                for l in labels:
                    print(str_text[l[0]:l[1]], l[2])
