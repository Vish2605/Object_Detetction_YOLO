import streamlit as st
import requests
import streamlit_lottie
import webbrowser
from BTP import predict
from BTP1 import predict1
import os
import cv2

def main():
    st.set_page_config(layout='wide')
    custom='''
    <style>
    body {
        background-color: #FFFFFF;
    }
    </style>
    '''

    st.markdown(custom,unsafe_allow_html=True)
    def lottie_loder(url):
        r=requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    l1=lottie_loder('https://lottie.host/2d2a270e-ef1d-4807-a036-0a66d706821d/7RwQtr9yJt.json')
    l2=lottie_loder('https://lottie.host/21920c70-d7d9-4dd4-b5a4-04de562eb120/IRBDqhEhDi.json')
    l3=lottie_loder('https://lottie.host/9c4fa02e-2a4c-4e7a-859d-5236799c1acf/oYYxKD5VVg.json')
    l4=lottie_loder('https://lottie.host/0f5b96b4-7819-43e6-a58c-b9b38cc199a7/SOZSDftnbK.json')
    l5=lottie_loder('https://lottie.host/ee487eb6-d68d-4dff-91f7-8f62f64720ba/RGYG6zCbY3.json')
    lottie_duct={1:l1,2:l2,3:l3}

    def open_website(website_url):
        webbrowser.open_new_tab(website_url)

    c1,c2,c3,c4,c5,c6=st.columns(6)
    with c1:
        st.markdown(
            f'<div style="font-size: 30px; font-weight: bold; color: #415056;text-align: center;">Quick-Links</div>',
            unsafe_allow_html=True
        )
    with c3:
        st.button("SK-learn",on_click=open_website,args=['https://scikit-learn.org/stable/'])
    with c4:

        st.button("Tensorflow",on_click=open_website, args=["https://www.tensorflow.org"])
    with c5:

        st.button("Neural-Networks",on_click=open_website,args=['https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/'],key="custom-button")
    with c6:
        st.button("OpenCV",on_click=open_website,args=['https://opencv.org/'])

    st.write('---')

    title='Helmet and License Plate Detection for Challan Imposition and Helmet Promotion'
    st.markdown(
        f'<div style="font-size: 80px; font-weight: bold; color: #1D5C96;text-align: center;">{title}</div>',
        unsafe_allow_html=True
    )

    st.write(' ')
    st.write(' ')

    left,right2 = st.columns(2)
    content='''
               Helmet and Number Plate Detection
Welcome to the Helmet and Number Plate Detection system! Our project is designed to enhance road safety and enforce traffic regulations by automating the detection of two critical aspects: helmet usage and vehicle number plates. By analyzing images and video streams, we can detect whether individuals are wearing helmets and identify vehicle number plates. We also assess the social score impact for those not complying with these rules.
             '''

    with left:
        st.write('')
        st.write('')
        st.write('')
        st.markdown(
            f'<div style="font-size: 28px;padding-top:70px;color: #687F8D;font-family: Pacifico, cursive;">{content}</div>',
            unsafe_allow_html=True
        )

    with right2:
        streamlit_lottie.st_lottie(l2)

    st.markdown(
        f'<div style="font-size: 35px; font-weight: bold; color: #1D5C96;">Upload Your Image</div>',
        unsafe_allow_html=True
    )

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        st.markdown(
            f'<div style="font-size: 25px; font-weight: bold; color: #1D5C96; justify-content: center;">Input Image</div>',
            unsafe_allow_html=True
        )
        st.image(uploaded_image, caption='Uploaded Image', width = 400)
        image_data = uploaded_image.read()
        output_directory = 'C:/Users/saura/OneDrive/Desktop/BTP/'
        output_filename = "uploaded_image.jpg"
        output_path = output_directory + output_filename

        with open(output_path, "wb") as f:
            f.write(image_data)
        output_img = predict(output_path)   
        
        st.markdown(
            f'<div style="font-size: 25px; font-weight: bold;  color: #1D5C96;justify-content: center;">Ouput Image</div>',
            unsafe_allow_html=True
        )
        st.image(output_img, caption='Uploaded Image', width = 400)
        predict1(output_path)
        os.remove(output_path)
        print("completed")

if __name__ == "__main__":
    main()
