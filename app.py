import streamlit as st
from pypdf import PdfReader

def convert_pdf_to_text(file_path: str) -> None:
    """
    This function converts PDF file to string. 
    Because email and name must appear on the first page so, return information only on the first page. 
    
    Args:
        file_path: path of pdf file
    """
    
    reader = PdfReader(file_path)

    page = reader.pages[0] # only on first page
    text = page.extract_text()
    
    text = text.replace("\n"," ")
    text = text.replace("\r", " ")
    text = " ".join(text.split(" "))
    return text 

@st.cache_resource()
def load_model():
    import spacy
    my_ner_model = spacy.load("output/model-best") #load the best model
    return my_ner_model

st.title("Named Entity Recognition")
st.write("Named Entity Recognition.")

model = load_model()
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")


if uploaded_file:
    # Read the PDF file
    with st.spinner("Please wait..."):
        text = convert_pdf_to_text(uploaded_file)

        predictions = model(text) # predict
        predictions = predictions.to_json()['ents']
        st.header("Output")

        for i in range(len(predictions)):
            result = predictions[i]
            start = result['start']
            end = result['end']
            label = result['label']
            text_result = text[start:end]

            if label == "Email":
                text_result = "".join(text_result.split(" "))
            
            st.text(f'{label}: {text_result}')
            
else:
    st.info("Please upload a PDF file.")
