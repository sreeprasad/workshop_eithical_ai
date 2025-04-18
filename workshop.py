import random
import time

study_buddy_name = "Buddy"

greeting_responses = [
    "Hi there! I'm {}, your study buddy!",
    "Hello! I'm {} and I'm here to help you learn!",
    "Hey! I'm {}. What would you like to study today?"
]

help_responses = [
    "I can help answer questions about math, science, history, and more!",
    "Ask me a homework question, and I'll try my best to help!",
    "I'm here to assist with your studies. What subject are you working on?"
]

confused_responses = [
    "I'm not sure I understand. Can you ask that another way?",
    "Hmm, I'm still learning and that's a bit confusing to me.",
    "Could you rephrase that question? I want to help but I'm not sure how."
]

knowledge_base = {
    "math": {
        "addition": "Addition means adding numbers together to find their sum.",
        "subtraction": "Subtraction is finding the difference between two numbers.",
        "multiplication": "Multiplication is repeated addition. For example, 3×4 means 3+3+3+3=12.",
        "division": "Division is splitting into equal parts or groups."
    },
    "science": {
        "water cycle": "The water cycle is the continuous movement of water within Earth: evaporation, condensation, and precipitation.",
        "planets": "Our solar system has eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
        "animals": "Animals can be classified into vertebrates (with backbones) and invertebrates (without backbones)."
    },
    "history": {
        "ancient egypt": "Ancient Egypt was a civilization along the Nile River known for pyramids, pharaohs, and hieroglyphics.",
        "world war 2": "World War II was a global conflict from 1939 to 1945 involving many of the world's nations."
    }
}

sensitive_topics = [
    "personal information",
    "harmful content",
    "cheating",
    "test answers",
    "complete assignments",
    "write essay",
    "write my",
    "do my",
    "do homework"
]

ethical_responses = [
    "I'm designed to help you learn, not to do the work for you.",
    "I can help you understand concepts, but completing assignments is your responsibility.",
    "Instead of giving you the answer, let me help you figure it out yourself.",
    "I shouldn't provide that information, but I can help you learn about this topic in a better way.",
    "Learning happens when you work through problems yourself. Let me guide you instead.",
    "As an ethical educational AI, I'm here to support your learning journey, not replace it."
]

learning_approaches = {
    "visual": "Let me explain this visually: imagine numbers or objects being combined when adding, separated when subtracting, grouped when multiplying, or divided into equal parts.",
    "step_by_step": "Let's break this down into smaller steps: first identify what we're working with, then apply the concept one step at a time, and finally check our understanding.",
    "example_based": "Here's a specific example: when studying ancient Egypt, we might examine how the pyramids were built, or how hieroglyphics were used for communication.",
    "question_based": "Let me ask you some questions to guide your thinking: How would you apply this concept to something in your daily life? What patterns do you notice?"
}

def get_greeting():
    """Returns a random greeting with the study buddy's name."""
    greeting = random.choice(greeting_responses)
    return greeting.format(study_buddy_name)

def search_knowledge_base(question):
    """Searches our knowledge base for an answer to the question."""
    question = question.lower()
    
    if question in knowledge_base:
        topics = list(knowledge_base[question].keys())
        return f"I know about these {question} topics: {', '.join(topics)}. Which one would you like to learn about?"
    
    for subject, topics in knowledge_base.items():
        if question == subject:
            topic_list = list(topics.keys())
            formatted_topics = ", ".join(topic_list)
            return f"I know about these {subject} topics: {formatted_topics}. Which one would you like to learn about?"
            
        for topic, information in topics.items():
            if topic in question:
                return information
    
    return None

def suggest_topic(question):
    """Suggests a related topic if no direct answer is found."""
    question = question.lower()
    
    for subject, topics in knowledge_base.items():
        if subject in question:
            return f"I don't know the specific answer, but I can tell you about {list(topics.keys())[0]} in {subject} if you're interested!"
    
    return None

def check_ethical_concerns(question):
    """Checks if the question raises any ethical concerns."""
    question = question.lower()
    
    for topic in sensitive_topics:
        if topic in question:
            return True
    
    if "give me the answer" in question or "what's the answer" in question:
        return True
        
    if "write my" in question or "do my" in question:
        return True
    
    return False

def determine_learning_style(question):
    """Determines the best learning style based on the question."""
    if "show" in question or "diagram" in question or "picture" in question:
        return "visual"
    elif "step" in question or "how to" in question:
        return "step_by_step"
    elif "example" in question:
        return "example_based"
    else:
        return random.choice(list(learning_approaches.keys()))

def respond_to_question(question):
    """Main function to respond to user questions."""
    time.sleep(0.5)
    
    question = question.lower().strip()
    
    if question == "":
        return "Please type a question or topic. You can ask about math, science, or history."
    
    if "hello" in question or "hi" in question:
        return get_greeting()
    
    if "help" in question or "what can you do" in question:
        return random.choice(help_responses)
    
    if check_ethical_concerns(question):
        return f"😕 {random.choice(ethical_responses)} Try asking me about a specific topic from our list instead!"
    
    answer = search_knowledge_base(question)
    if answer:
        learning_style = determine_learning_style(question)
        if learning_style in learning_approaches:
            return f"😊 {answer} {learning_approaches[learning_style]}"
        return f"😊 {answer}"
    
    suggestion = suggest_topic(question)
    if suggestion:
        return f"🤔 {suggestion}"
    
    confused_response = random.choice(confused_responses)
    return f"🤔 {confused_response} Try asking about one of the topics I mentioned at the beginning!"

def main():
    """Main function to run our study buddy."""
    print(get_greeting())
    print("Type 'exit' when you're done.")
    print("Here are some topics you can ask me about:")
    
    for subject, topics in knowledge_base.items():
        topic_list = list(topics.keys())
        formatted_topics = ", ".join(topic_list)
        print(f"- {subject.title()} topics: {formatted_topics}")
    
    print("You can also try asking unethical questions to see how I respond!")
    print("For example: 'write my essay' or 'give me test answers'")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print(f"{study_buddy_name}: Goodbye! Happy studying!")
            break
        
        response = respond_to_question(user_input)
        print(f"{study_buddy_name}: {response}")

if __name__ == "__main__":
    main()
