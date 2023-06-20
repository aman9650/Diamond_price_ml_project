import pickle
import streamlit as st
model = pickle.load(open('random_forest_model.pkl','rb'))

def main():
    st.title('Diamond Price prediction')

    # input variable
    carat = st.text_input('carat')
    clarity=st.text_input('clarity')

    #prediction code
    if st.button('predict'):
         makeprediction = model.predict([[carat,clarity]])
         output=round(makeprediction[0],2)
         st.success('the price for the diamond is {}'.format(output))
if __name__=='__main__' :
    main()


