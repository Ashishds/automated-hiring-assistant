import asyncio
from typing import List

# Simple mock interview chat for testing
async def main():
    print("🤖 Welcome to the Recruiter Agent Interview Chat!")
    print("=" * 50)
    print("This is a simplified version for testing.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("=" * 50)
    
    message_history = []
    candidate_response = ""
    
    # Chat loop
    while True:
        if candidate_response.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Interview ended.")
            break
        
        if not message_history:
            print("🤖 Interviewer: Hello! Welcome to our technical interview. Could you please introduce yourself and tell me about your background?")
            candidate_response = input("\n👤 You: ")
            message_history.append({"role": "user", "content": candidate_response})
        else:
            # Simple mock interviewer responses
            mock_responses = [
                "That's interesting! Can you tell me more about your experience with that technology?",
                "Great! How would you approach solving a challenging problem in that area?",
                "Excellent answer! What's your experience with version control systems?",
                "Very good! How do you stay updated with the latest technologies?",
                "Impressive! Do you have any questions for me about the role or company?"
            ]
            
            response_index = len(message_history) % len(mock_responses)
            interviewer_response = mock_responses[response_index]
            
            print(f"\n🤖 Interviewer: {interviewer_response}")
            message_history.append({"role": "assistant", "content": interviewer_response})
            
            candidate_response = input("\n👤 You: ")
            message_history.append({"role": "user", "content": candidate_response})
    
    print(f"\n📊 Interview Summary:")
    print(f"Total exchanges: {len(message_history)}")
    print("Thank you for participating in this interview simulation!")

if __name__ == "__main__":
    asyncio.run(main())


