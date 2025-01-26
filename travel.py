import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def get_response(prompt):
    """Fetch response from OpenAI API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI-powered travel planner."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def generate_itinerary(destination, travel_dates, travel_style, interests, accommodation, transport, pace):
    """Generate a travel itinerary based on user inputs."""
    prompt = f"""
    Create a detailed, personalized travel itinerary for:
    - Destination: {destination}
    - Travel Dates: {travel_dates}
    - Travel Style: {travel_style}
    - Interests: {interests}
    - Accommodation Preference: {accommodation}
    - Transport Preference: {transport}
    - Daily Activity Pace: {pace}

    Include specific activities, restaurants, and transportation options for each day.
    """
    return get_response(prompt)

# Streamlit App
def main():
    st.title("AI-Powered Travel Planner")
    st.subheader("Plan your perfect trip with personalized itineraries!")

    # Step 1: Gather User Preferences
    with st.form("user_preferences_form"):
        destination = st.text_input("Where are you planning to travel?")
        travel_dates = st.text_input("What are your travel dates or duration?")
        travel_style = st.selectbox("What’s your travel style?", ["Adventure", "Relaxation", "Cultural", "Mixed"])
        interests = st.text_input("What are your interests? (e.g., food, hiking, history)")
        accommodation = st.selectbox("Preferred accommodation type", ["Hotel", "Hostel", "Airbnb", "Other"])
        transport = st.selectbox("Preferred transport method", ["Public transport", "Car rental", "Mixed"])
        pace = st.selectbox("What’s your ideal daily activity pace?", ["Packed", "Moderate", "Relaxed"])
        submit = st.form_submit_button("Generate Itinerary")

    if submit:
        if not destination or not travel_dates:
            st.error("Please fill in all required fields.")
        else:
            st.write("Generating your personalized itinerary...")
            itinerary = generate_itinerary(destination, travel_dates, travel_style, interests, accommodation, transport, pace)
            st.success("Here’s your travel itinerary:")
            st.write(itinerary)

    # Optional feedback loop
    st.subheader("Want to modify your itinerary?")
    feedback = st.text_input("Describe any changes or adjustments you'd like:")
    if st.button("Update Itinerary"):
        updated_prompt = f"The user wants to modify the itinerary as follows: {feedback}. Update the original itinerary accordingly."
        updated_itinerary = get_response(updated_prompt)
        st.write("Here’s your updated itinerary:")
        st.write(updated_itinerary)

if __name__ == "__main__":
    main()
