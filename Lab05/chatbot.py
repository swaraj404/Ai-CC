import streamlit as st
# Page settings
st.set_page_config(page_title="Amazon Chatbot", page_icon="🛒", layout="centered")
# Title
st.title("🛒 Amazon Customer Support Chatbot")
st.write("Welcome! Ask me anything about your orders, returns, payments, or Prime.")
# Sidebar
st.sidebar.title("📌 Menu")
st.sidebar.info("Amazon Support Bot\nVersion 1.0")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Function to generate bot response
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I assist you today?"
    elif "order" in user_input and "status" in user_input:
        return "📦 Please enter your Order ID (e.g., AMZ12345)."
    elif "cancel" in user_input:
        return "❌ To cancel an order, go to 'Your Orders' and click 'Cancel Item'."
    elif "return" in user_input or "refund" in user_input:
        return "🔁 Items can be returned within 7 days. Refund will be processed in 3-5 business days."
    elif "product" in user_input:
        return "🛍️ We have electronics, fashion, home items and more. What are you looking for?"
    elif "prime" in user_input:
        return "⭐ Amazon Prime gives free delivery, exclusive deals, and streaming services."
    elif "payment" in user_input:
        return "💳 We support UPI, credit/debit cards, net banking, and Cash on Delivery."
    elif "contact" in user_input or "support" in user_input:
        return "📞 You can contact support via the Help section in the Amazon app or website."
    elif "order id" in user_input:
        return "✅ Your order is out for delivery and will arrive soon!"
    else:
        return "🤖 Sorry, I didn’t understand that. Please try asking something else."
# Chat input
user_input = st.chat_input("Type your message here...")
# Handle user input
if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    # Generate and display bot response
    response = get_bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
