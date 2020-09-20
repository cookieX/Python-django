from Legal.api.Continent import Continue
import re
import docx   

# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)


def text_file(files):
    filename = files.name
    ext = filename.split('.')[-1]
    if ext == "txt":
        with open(files, 'r') as file:
            return file.read().replace('\n', '')
    # elif ext == "docx" or "doc" or "docm":
    #     return getText(files)
    elif ext == "pdf":
        rawText = parser.from_file(files)
        return rawText['content'].splitlines()
    else:
        pass

def GetConti(counry):
    if counry in Continue['asia']:
        return "Asia"
    elif counry in Continue['europe']:
        return "Europe"
    elif counry in Continue['africa']:
        return "Africa"
    elif counry in Continue['North America']:
        return "North America"
    elif counry in Continue['South America']:
        return "South America"
    elif counry in Continue['South America']:
        return "Oceania"
    else:
        return "other"



def multisub(subs, subject):
    "Simultaneously perform all substitutions on the subject string."
    pattern = '|'.join('(%s)' % re.escape(p) for p, s in subs)
    substs = [s for p, s in subs]
    replace = lambda m: substs[m.lastindex - 1]
    return re.sub(pattern, replace, subject)