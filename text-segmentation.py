import  re

caps = "([ஃ-்])"
prefixes = "(திரு|புனித|திருமதி|செல்வி|கலாநிதி)[.]"
suffixes = "(Inc|லிமிடட்|Jr|Sr|Co)"
starters = "(திரு|திருமதி|செல்வி|கலாநிதி|அவன்\s|அவள்\s|அவை\s|அவா்கள்\s|அவா்களுடைய\s|எங்களுடைய\s|நாங்கள்\s|ஆனால்\s|எப்படியாயினும்\s|அது\s|இது\s|எங்கேயாயினும்)"
acronyms = "([ஃ-்][.][ஃ-்][.](?:[ஃ-்][.])?)"
websites = "[.](com|net|org|io|gov)"
period="([ஃ-்][(ி|ு)])"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    text = re.sub(period + "[.]"+ period + "[.]","\\1<prd>\\2<prd>", text)
    if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + caps + "[.]", " \\1<prd>", text)
    if "\"" in text: text = text.replace(".\"", "\".")
    if "!" in text: text = text.replace("!\"", "\"!")
    if "?" in text: text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

#text="சென்னை நகருக்கு நீண்ட வரலாறு உள்ளது. மு.ப. 1ஆம் நூற்றாண்டு முதல் பல்லவ, சோழ மற்றும் விஜயநகர பேரரசுகளில் சென்னை ஒரு முக்கிய இடமாக விளங்கியதாகக் கருதப்படுகிறது."
#print(split_into_sentences(text))