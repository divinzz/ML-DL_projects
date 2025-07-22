import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import pairwise_distances
from PIL import Image

def load_data():
    boys_extracted_features = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Boys_ResNet_features.npy')
    boys_Productids = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Boys_ResNet_feature_product_ids.npy')

    girls_extracted_features = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Girls_ResNet_features.npy')
    girls_Productids = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Girls_ResNet_feature_product_ids.npy')

    men_extracted_features = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Men_ResNet_features.npy')
    men_Productids = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Men_ResNet_feature_product_ids.npy')

    women_extracted_features = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Women_ResNet_features.npy')
    women_Productids = np.load(r'C:\\Users\\ACER\\Documents\\ml prjt\\Fashion Recommendation\\Women_ResNet_feature_product_ids.npy')

    fashion_df = pd.read_csv(r"C:\Users\ACER\Downloads\product recommander\data\fashion.csv")
    fashion_df["ProductId"] = fashion_df["ProductId"].astype(str)

    return boys_extracted_features, boys_Productids, girls_extracted_features, girls_Productids, men_extracted_features, men_Productids, women_extracted_features, women_Productids, fashion_df

def get_similar_products(product_id, num_results, fashion_df, boys_extracted_features, boys_Productids, girls_extracted_features, girls_Productids, men_extracted_features, men_Productids, women_extracted_features, women_Productids):
    gender_category = fashion_df[fashion_df['ProductId'] == product_id]['Gender'].values[0]
    
    if gender_category == "Boys":
        extracted_features = boys_extracted_features
        product_ids = boys_Productids
    elif gender_category == "Girls":
        extracted_features = girls_extracted_features
        product_ids = girls_Productids
    elif gender_category == "Men":
        extracted_features = men_extracted_features
        product_ids = men_Productids
    elif gender_category == "Women":
        extracted_features = women_extracted_features
        product_ids = women_Productids

    product_ids = list(product_ids)
    
    try:
        doc_id = product_ids.index(product_id)
    except ValueError:
        st.write(f"Product ID {product_id} not found.")
        return []

    pairwise_dist = pairwise_distances(extracted_features, extracted_features[doc_id].reshape(1, -1))
    
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    pdists = np.sort(pairwise_dist.flatten())[0:num_results]
    
    valid_indices = [i for i in indices if i < len(product_ids)]
    valid_pdists = pdists[:len(valid_indices)] 
    similar_products = []
    for i in range(1, len(valid_indices)):  
        rows = fashion_df[['ImageURL', 'ProductTitle']].loc[fashion_df['ProductId'] == product_ids[valid_indices[i]]]
        for indx, row in rows.iterrows():
            similar_products.append({
                'image_url': row['ImageURL'],
                'product_title': row['ProductTitle'],
                'distance': valid_pdists[i]  
            })
    
    return similar_products, gender_category

def main():
    st.title("Fashion Product Recommendation System")
    st.write("Enter a Product ID to see similar products.")
    
    boys_extracted_features, boys_Productids, girls_extracted_features, girls_Productids, men_extracted_features, men_Productids, women_extracted_features, women_Productids, fashion_df = load_data()

    all_product_ids = fashion_df['ProductId'].astype(str).tolist()

    if 'product_id_input' not in st.session_state:
        st.session_state.product_id_input = ""

    product_id_input = st.selectbox("Select a Product ID", options=all_product_ids, index=all_product_ids.index(st.session_state.product_id_input) if st.session_state.product_id_input else 0)

    st.session_state.product_id_input = product_id_input

    if st.button("Get Similar Products"):
        if st.session_state.product_id_input:
            similar_products, gender_category = get_similar_products(st.session_state.product_id_input, num_results=6, fashion_df=fashion_df, 
                                                                     boys_extracted_features=boys_extracted_features, boys_Productids=boys_Productids,
                                                                     girls_extracted_features=girls_extracted_features, girls_Productids=girls_Productids,
                                                                     men_extracted_features=men_extracted_features, men_Productids=men_Productids,
                                                                     women_extracted_features=women_extracted_features, women_Productids=women_Productids)

            if similar_products:
                category_products_count = len(fashion_df[fashion_df['Gender'] == gender_category])
                st.write(f"Total number of products in {gender_category} category: {category_products_count}")
                
                st.write("="*20 + " Input Product " + "="*20)
                input_product = fashion_df[fashion_df['ProductId'] == st.session_state.product_id_input].iloc[0]
                st.image(input_product['ImageURL'], width=224, caption=input_product['ProductTitle'])
                
                st.write("="*20 + " Recommended Products " + "="*20)

                st.markdown("""
                    <style>
                        .stColumn {
                            margin-right: 20px;
                            margin-left: 20px;
                        }
                    </style>
                """, unsafe_allow_html=True)

                num_columns = 5
                columns = st.columns(num_columns)

                for i, product in enumerate(similar_products):
                    column_index = i % num_columns  
                    with columns[column_index]:
                        st.image(product['image_url'], width=224, caption=product['product_title'])

        else:
            st.write("Please enter a valid Product ID.")

if __name__ == "__main__":
    main()
