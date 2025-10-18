import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key=st.secrets.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="AI Prompt Generator", page_icon="⚡")
st.title("⚡ CodePromptX — AI Prompt Generator")
st.caption("Powered by GroqCloud (Free Model: groq/compound-mini)")

# Input box
topic = st.text_input("Enter your idea or topic:", placeholder="e.g. AI logo design, startup pitch, YouTube title...")

# Generate button
if st.button("Generate Prompts 🚀"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="groq/compound-mini",
                const messages = [
  {
    role: "system",
    content: "You are an expert AI prompt generator. Provide short, precise, and highly relevant prompts that a professional could immediately use. Avoid fluff or generic suggestions."
  },
  {
    role: "user",
    content: `Given the topic "${topic}", generate 3 clear, actionable, and authentic prompts that directly relate to this subject. Each prompt should be unique and useful for practical implementation.`
  }
];

            )
            output = response.choices[0].message.content
        st.subheader("✨ Your AI-Generated Prompts")
        st.write(output)

st.divider()
st.caption("💡 Tip: Try topics like 'AI art', 'marketing post', 'logo concept', or 'automation script'.")
