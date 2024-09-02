import pickle
import streamlit as st
import numpy as np
pickle_in=open("Model_dt_Final.pkl","rb")
model=pickle.load(pickle_in)
@st.cache_data
def predict_cancer(Age,Chest_Pain,Cholestrol_level,Patient_max_count,Depression_level,Fluoroscopy_status,Thallium_value):
    input=np.array([[Age,Chest_Pain,Cholestrol_level,Patient_max_count,Depression_level,Fluoroscopy_status,Thallium_value]])
    prediction=model.predict(input)
    return prediction
def main():
    st.title("Heart Disease Prediction")
    image_path=r"C:\Users\pspto\Desktop\Demo\Heart2.jpg"
    st.image(image_path,caption="HEART DISEASE",use_column_width=True)
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    Name=st.text_input('Enter Patient Name')
    Gender=st.selectbox('Gender',("Male","Female"))
    Age=st.slider('Enter Patient Age',0,100,25)
    Chest_Pain=st.slider('Enter Patient Chest Pain status',0,3,0)
    Cholestrol_level=st.slider('Enter Patient Cholestrol Level status',126,564,0)
    Patient_max_count=st.slider('Enter Patient Max Count status',71,202,0)
    Depression_level=st.number_input('Enter Patient Depression Level status',min_value=0,max_value=6)
    Fluoroscopy_status=st.slider('Enter Patient Fluoroscopy status',0,4,0)
    Thallium_value=st.slider('Enter Patient Thallium Value status',0,3,0)
    output=""
    text=""
    safe_html ="""  
    <div style="background-color:#80ff80; padding:10px >
    <h2 style="color:white;text-align:center;"> The Abalone is young</h2>
    </div>
    """
    if st.button("Predict"):
        output=predict_cancer(Age,Chest_Pain,Cholestrol_level,Patient_max_count,Depression_level,Fluoroscopy_status,Thallium_value)
        if output==0:
            text='NEGATIVE'
        else:
            text='POSITIVE'
    st.success(f"Patient {Name} Cardic Status {text}")
if __name__=='__main__':
    main()