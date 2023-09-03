""" Write a function that takes a string as input and uses the spacy library to extract Named Entities of that string. Then, tag all occurrences of names (labelled as 'PERSON') with brackets [] and location with {}. Check the screenshot for more clarity. """


# install required packages if needed (spacy and its pre-trained model "en_core_web_sm")

# !pip install spacy
# import spacy
# spacy.cli.download("en_core_web_sm")

def loc_per_spacy(text):
    import spacy
    sp_mod=spacy.load("en_core_web_sm")
    doc = sp_mod(text)
    person = [ent.text for ent in doc.ents if ent.label_=="PERSON"]
    location = [ent.text for ent in doc.ents if ent.label_ == "LOC" or ent.label_=="GPE"]
    out_text=""
    for word in person:
      ind = text.find(word)
      if ind != -1:
        out_text=text[:ind]+"["+word+"]"+text[ind+len(word):]
    for word in location:
      ind = out_text.find(word)
      if ind != -1:
        out_text=out_text[:ind]+"{"+word+"}"+out_text[ind+len(word):]
    return out_text

loc_per_spacy("John visited Paris last summer.")
