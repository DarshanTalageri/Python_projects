import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="DBOSS Restaurant")
st.title("🍽️ Welcome to DBOSS Restaurant")
st.subheader("Menu:")

# --- Menu items ---
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 80,
}

# --- Show the menu ---
for item, price in menu.items():
    st.write(f"- {item}: ₹{price}")

# --- Initialize session state ---
if "order_total" not in st.session_state:
    st.session_state.order_total = 0
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# --- First item selection ---
item_1 = st.selectbox("Select your first item", list(menu.keys()))
if st.button("Add First Item"):
    st.session_state.order_total += menu[item_1]
    st.session_state.selected_items.append(item_1)
    st.success(f"{item_1} added to your order! Current total: ₹{st.session_state.order_total}")

# --- Optional second item ---
if st.checkbox("Do you want to add another item?"):
    item_2 = st.selectbox("Select your second item", list(menu.keys()), key="item2")
    if st.button("Add Second Item"):
        st.session_state.order_total += menu[item_2]
        st.session_state.selected_items.append(item_2)
        st.success(f"{item_2} added! Current total: ₹{st.session_state.order_total}")

# --- Show total ---
if st.button("Show Total"):
    if st.session_state.selected_items:
        st.info(f"Items ordered: {', '.join(st.session_state.selected_items)}")
        st.success(f"Total amount to pay: ₹{st.session_state.order_total}")
    else:
        st.warning("You haven't ordered anything yet!")
