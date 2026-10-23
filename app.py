
# AI Customer Support Agent - Complete Version

from ticket_manager import (
    create_ticket,
    view_tickets,
    search_ticket,
    update_ticket_status,
    ticket_summary,
    search_tickets_by_priority,
    view_unresolved_tickets,
    count_unresolved_tickets,
    ticket_dashboard,
    search_tickets_by_issue,
    collect_feedback,
    view_feedback,
    calculate_average_rating,
    project_status_report,
)

from gemini_helper import (
    ask_gemini,
    AI_ERROR_MESSAGE,
    conversation_history,
)


# Rule-based customer support answers
support_answers = {
    "hello": "Hello! Welcome to customer support. How can I help you?",
    "hi": "Hi! How can I help you today?",
    "hey": "Hello! How can I assist you?",
    "refund": "For a refund, please share your order details with our support team.",
    "payment": "Please check your payment status. If the amount was deducted but the order failed, our support team can help.",
    "delivery": "Please check your order tracking page for the latest delivery status.",
    "tracking": "You can check your order tracking page for delivery updates.",
    "order": "I can help with your order. For tracking updates, please check your order tracking page. If you still need help, tell me more about your issue.",
    "account": "Please check your account details. If the issue continues, contact our support team.",
    "password": "If you forgot your password, use the Forgot Password option to reset it.",
    "contact": "You can create a support ticket so our team can review your issue.",
}


# Get a response using simple rules or Gemini AI
def get_response(message):
    message_lower = message.lower().strip()

    for keyword, answer in support_answers.items():
        if keyword in message_lower:
            return answer

    # Use Gemini for questions not covered by the rules
    return ask_gemini(message)


# Ask the user to select a ticket status
def choose_ticket_status(ticket_id):
    print("\nChoose the new ticket status:")
    print("1. Open")
    print("2. Pending")
    print("3. Resolved")

    choice = input("Enter your choice (1-3): ").strip()

    status_options = {
        "1": "Open",
        "2": "Pending",
        "3": "Resolved",
    }

    if choice in status_options:
        update_ticket_status(ticket_id, status_options[choice])
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


# Display available commands
def show_help():
    print("\n========== CUSTOMER SUPPORT HELP ==========")
    print("help - Display available commands")
    print("view tickets - View all support tickets")
    print("create ticket - Create a support ticket")
    print("search ticket - Search a ticket by ID")
    print("update ticket - Update a ticket status")
    print("ticket summary - View ticket summary")
    print("ticket dashboard - View ticket statistics")
    print("search by priority - Search tickets by priority")
    print("search by issue - Search tickets using a keyword")
    print("view unresolved tickets - View unresolved tickets")
    print("count unresolved tickets - Count unresolved tickets")
    print("give feedback - Submit customer feedback")
    print("view feedback - View saved customer feedback")
    print("average rating - Calculate average customer rating")
    print("project report - View the project status report")
    print("new conversation - Clear Gemini conversation history")
    print("bye - Exit the chatbot")
    print("============================================")


# Main chatbot function
def run_chatbot():
    print("\n========================================")
    print(" Welcome to AI Customer Support Agent!")
    print(" Type 'help' to see available commands.")
    print(" Type 'bye' to exit.")
    print("========================================")

    while True:
        try:
            message = input("\nCustomer: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nThank you for using customer support. Goodbye!")
            break

        if not message:
            print("Please enter a message.")
            continue

        command = message.casefold()

        # Exit chatbot
        if command in ["bye", "exit", "quit"]:
            print("Thank you for using customer support. Goodbye!")
            break

        # Display help
        elif command == "help":
            show_help()
            continue

        # Start a new Gemini conversation
        elif command == "new conversation":
            conversation_history.clear()
            print("Conversation history cleared. Let's start fresh!")
            continue

        # Create support ticket
        elif command == "create ticket":
            issue = input("Describe your issue: ").strip()

            if issue:
                create_ticket(issue)
            else:
                print("Issue cannot be empty.")

            continue

        # View all tickets
        elif command in ["view ticket", "view tickets"]:
            view_tickets()
            continue

        # Search ticket by ID
        elif command == "search ticket":
            ticket_id = input("Enter ticket ID: ").strip()
            search_ticket(ticket_id)
            continue

        # Update ticket status
        elif command == "update ticket":
            ticket_id = input("Enter ticket ID: ").strip()
            choose_ticket_status(ticket_id)
            continue

        # View ticket summary
        elif command == "ticket summary":
            ticket_summary()
            continue

        # View ticket dashboard
        elif command == "ticket dashboard":
            ticket_dashboard()
            continue

        # Search tickets by priority
        elif command == "search by priority":
            priority = input(
                "Enter priority (High, Medium, Low): "
            ).strip()

            search_tickets_by_priority(priority)
            continue

        # Search tickets by issue keyword
        elif command == "search by issue":
            keyword = input("Enter a keyword to search: ").strip()
            search_tickets_by_issue(keyword)
            continue

        # View unresolved tickets
        elif command == "view unresolved tickets":
            view_unresolved_tickets()
            continue

        # Count unresolved tickets
        elif command == "count unresolved tickets":
            count_unresolved_tickets()
            continue

        # Collect customer feedback
        elif command == "give feedback":
            collect_feedback()
            continue

        # View saved customer feedback
        elif command == "view feedback":
            view_feedback()
            continue

        # Calculate average rating
        elif command == "average rating":
            calculate_average_rating()
            continue

        # Display combined project report
        elif command == "project report":
            project_status_report()
            continue

        # Handle ordinary customer messages
        response = get_response(message)
        print(f"\nBot: {response}")

        # Handle Gemini API errors
        if response == AI_ERROR_MESSAGE:
            print("\nWhat would you like to do?")
            print("1. Retry the question")
            print("2. Create a support ticket")
            print("3. Continue")

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                retry_response = ask_gemini(message)
                print(f"\nBot: {retry_response}")

            elif choice == "2":
                create_ticket(message)

            elif choice == "3":
                print("You can continue asking questions.")

            else:
                print("Invalid choice. You can continue chatting.")

        else:
            # Offer a ticket if the customer still needs assistance
            choice = input(
                "\nWould you like to create a support ticket? (yes/no): "
            ).strip().lower()

            if choice in ["bye", "exit", "quit"]:
                print("Goodbye! Have a great day.")
                break

            if choice in ["yes", "y"]:
                create_ticket(message)

            elif choice in ["no", "n"]:
                print("Okay! Let me know if you need anything else.")

            else:
                print("You can continue chatting whenever you're ready.")


# Start the chatbot
if __name__ == "__main__":
    run_chatbot()
