# Save this file as 'app.py'
from flask import Flask, request, jsonify
from flask_cors import CORS
# Note: You will need to install these libraries: pip install Flask Flask-CORS

app = Flask(__name__)
# Enable CORS to allow the HTML file (running in your browser) to communicate with this server
CORS(app) 

# --- Function to Scrape and Answer (Conceptual Logic) ---
# NOTE: This is a keyword-based logic. For true URL data reading, 
# you would replace this with a powerful LLM like Gemini or a complex RAG pipeline.
def get_college_info(query):
    query = query.lower()

    if "admission" in query or "apply" in query or "process" in query:
        return "The admission process for UG courses is strictly merit-based on 10+2 marks. PG courses may require valid entrance scores (e.g., NMAT for MBA). All applications must be submitted **online** via the official Yadhava College portal."
    
    elif "fee" in query or "cost" in query:
        return "The fees structure varies between **Aided** and **Self-Finance** courses. Please check the official 'Fees Structure' page on the college website for the specific course you are interested in."
    
    elif "scholarship" in query or "scheme" in query:
        return "Yadhava College students are eligible for various **Central and State Government Scholarships** (e.g., BC, SC Welfare). Eligibility criteria are strictly enforced. Details are available on the 'Scholarship' menu."

    elif "course" in query or "courses" in query or "departments" in query:
        return "Yadhava College offers a wide range of UG and PG programs, including B.Sc. (Physics, Computer Science, IT), B.Com., B.A., M.Sc., and M.Com. Please specify the course level (UG/PG) or subject for detailed **course outcomes**."
        
    elif "history" in query or "established" in query:
        return "Yadhava College was established in **1969** to uplift the educational standards of the community, and it is an Autonomous Institution affiliated with Madurai Kamaraj University."

    elif "contact" in query or "location" in query or "address" in query:
        return "You can find all contact information and the college address on the official **'Contact Us'** page. The college is located in Tiruppalai, Madurai."
        
    elif "hi" in query or "hello" in query:
        return "Hello! I am the Yadhava College Bot. I can answer questions about admissions, fees, and courses based on the data from the college website. How can I assist you today?"
    
    else:
        return f"I couldn't find a direct answer for your query about '{query}' in my current knowledge base. I can better assist with questions about **Admissions, Fees, Courses, or History**."

# --- API Endpoint ---
@app.route('/api/chat', methods=['POST'])
def chat():
    # Read the user's question from the frontend
    user_query = request.json.get('query', '')
    
    # Get the synthesized answer from the function above
    answer = get_college_info(user_query)

    # Return the answer to the frontend
    return jsonify({'answer': answer})

if __name__ == '__main__':
    print("Starting Yadhava College Chatbot Backend...")
    print("Make sure to open index.html in your browser.")
    # Runs the server on port 5000
    app.run(debug=True, port=5000)
