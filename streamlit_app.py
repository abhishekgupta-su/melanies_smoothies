# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f"My Parents New Healthy Diner")
st.write(
  """Breakfast Menu
  Omega 3 & Blueberry Oatmeal
  Kale, Spinach & Rocket Smoothie
  Hard-Boiled Free-Range Egg
  """
)

#name_on_order = st.text_input("Name on Smoothie")
#st.write("The name on your Smoothie will be: ", name_on_order)

#cnx = st.connection("snowflake")
#session = get_active_session()
#session = cnx.session()
#my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

#ingredients_list = st.multiselect('Choose up to 5 ingredients:', my_dataframe, max_selections=5)

#if ingredients_list:
#    ingredients_string = ''

#    for fruit_chosen in ingredients_list:
#        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

#    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
#            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)
    #st.stop()
#time_to_insert = st.button('Submit Order')

#if time_to_insert:
#    session.sql(my_insert_stmt).collect()
    
#    st.success('Your Smoothie is ordered!', icon="✅")
