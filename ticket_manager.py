
TICKET_FILE = "tickets.txt"
FEEDBACK_FILE = "feedback.txt"
SEPARATOR = "----------------------------"


# Create a support ticket
def create_ticket(message):
    message = message.strip()

    if not message:
        print("Please enter a valid issue.")
        return

    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = ""

    # Avoid duplicate issues
    existing_tickets = content.split(SEPARATOR)

    for ticket in existing_tickets:
        for line in ticket.splitlines():
            if line.startswith("Customer Issue:"):
                old_issue = line.split(":", 1)[1].strip()
                if old_issue.casefold() == message.casefold():
                    print("A ticket for this issue already exists.")
                    return

    ticket_id = content.count("Ticket ID:") + 1

    issue_lower = message.casefold()

    high_keywords = [
        "payment failed", "fraud", "urgent", "charged twice"
    ]
    medium_keywords = [
        "delivery", "order", "refund", "tracking", "late"
    ]

    if any(word in issue_lower for word in high_keywords):
        priority = "High"
    elif any(word in issue_lower for word in medium_keywords):
        priority = "Medium"
    else:
        priority = "Low"

    with open(TICKET_FILE, "a", encoding="utf-8") as file:
        if content and not content.endswith("\n"):
            file.write("\n")

        file.write(f"Ticket ID: {ticket_id}\n")
        file.write(f"Customer Issue: {message}\n")
        file.write(f"Priority: {priority}\n")
        file.write("Status: Open\n")
        file.write(SEPARATOR + "\n")

    print("\nSupport ticket created successfully!")
    print(f"Ticket ID: {ticket_id}")
    print(f"Priority: {priority}")
    print("Status: Open")


# View all support tickets
def view_tickets():
    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip():
            print("\n--- All Support Tickets ---")
            print(content)
        else:
            print("No support tickets available.")

    except FileNotFoundError:
        print("No support tickets available.")


# Search a ticket by ID
def search_ticket(ticket_id):
    ticket_id = str(ticket_id).strip()

    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No support tickets available.")
        return

    for ticket in content.split(SEPARATOR):
        for line in ticket.splitlines():
            if line.startswith("Ticket ID:"):
                saved_id = line.split(":", 1)[1].strip()

                if saved_id == ticket_id:
                    print("\n--- Ticket Found ---")
                    print(ticket.strip())
                    return

    print("Ticket ID not found.")


# Update ticket status
def update_ticket_status(ticket_id, new_status):
    ticket_id = str(ticket_id).strip()
    new_status = new_status.strip().capitalize()

    if new_status not in ["Open", "Pending", "Resolved"]:
        print("Invalid status. Use Open, Pending, or Resolved.")
        return

    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No support tickets available.")
        return

    tickets = content.split(SEPARATOR)
    updated = False

    for index, ticket in enumerate(tickets):
        lines = ticket.splitlines()

        for line_index, line in enumerate(lines):
            if line.startswith("Ticket ID:"):
                saved_id = line.split(":", 1)[1].strip()

                if saved_id == ticket_id:
                    status_found = False

                    for i, saved_line in enumerate(lines):
                        if saved_line.startswith("Status:"):
                            lines[i] = f"Status: {new_status}"
                            status_found = True
                            break

                    if not status_found:
                        lines.append(f"Status: {new_status}")

                    tickets[index] = "\n".join(lines)
                    updated = True
                    break

        if updated:
            break

    if not updated:
        print("Ticket ID not found.")
        return

    updated_content = SEPARATOR.join(tickets)

    with open(TICKET_FILE, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Ticket {ticket_id} status updated to {new_status}.")


# Display ticket summary
def ticket_summary():
    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = ""

    tickets = [
        ticket for ticket in content.split(SEPARATOR)
        if "Ticket ID:" in ticket
    ]

    total = len(tickets)
    open_count = 0
    pending_count = 0
    resolved_count = 0

    for ticket in tickets:
        if "Status: Open" in ticket:
            open_count += 1
        elif "Status: Pending" in ticket:
            pending_count += 1
        elif "Status: Resolved" in ticket:
            resolved_count += 1

    print("\n--- Ticket Summary ---")
    print(f"Total tickets: {total}")
    print(f"Open tickets: {open_count}")
    print(f"Pending tickets: {pending_count}")
    print(f"Resolved tickets: {resolved_count}")


# Search tickets by priority
def search_tickets_by_priority(priority):
    priority = priority.strip().capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Choose High, Medium, or Low.")
        return

    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No support tickets available.")
        return

    found = False

    print(f"\n--- {priority} Priority Tickets ---")

    for ticket in content.split(SEPARATOR):
        if "Ticket ID:" in ticket and f"Priority: {priority}" in ticket:
            print(ticket.strip())
            print(SEPARATOR)
            found = True

    if not found:
        print(f"No {priority} priority tickets found.")


# View unresolved tickets
def view_unresolved_tickets():
    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No support tickets available.")
        return

    found = False
    print("\n--- Unresolved Tickets ---")

    for ticket in content.split(SEPARATOR):
        if "Ticket ID:" in ticket and (
            "Status: Open" in ticket or "Status: Pending" in ticket
        ):
            print(ticket.strip())
            print(SEPARATOR)
            found = True

    if not found:
        print("No unresolved tickets found.")


# Count unresolved tickets
def count_unresolved_tickets():
    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = ""

    count = 0

    for ticket in content.split(SEPARATOR):
        if "Ticket ID:" in ticket and (
            "Status: Open" in ticket or "Status: Pending" in ticket
        ):
            count += 1

    print(f"Total unresolved tickets: {count}")


# Display ticket dashboard
def ticket_dashboard():
    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = ""

    tickets = [
        ticket for ticket in content.split(SEPARATOR)
        if "Ticket ID:" in ticket
    ]

    high = 0
    medium = 0
    low = 0
    open_count = 0
    pending = 0
    resolved = 0

    for ticket in tickets:
        if "Priority: High" in ticket:
            high += 1
        elif "Priority: Medium" in ticket:
            medium += 1
        elif "Priority: Low" in ticket:
            low += 1

        if "Status: Open" in ticket:
            open_count += 1
        elif "Status: Pending" in ticket:
            pending += 1
        elif "Status: Resolved" in ticket:
            resolved += 1

    print("\n========== TICKET DASHBOARD ==========")
    print(f"Total tickets: {len(tickets)}")
    print(f"High priority: {high}")
    print(f"Medium priority: {medium}")
    print(f"Low priority: {low}")
    print(f"Open tickets: {open_count}")
    print(f"Pending tickets: {pending}")
    print(f"Resolved tickets: {resolved}")
    print("======================================")


# Search tickets by issue keyword
def search_tickets_by_issue(keyword):
    keyword = keyword.strip().casefold()

    if not keyword:
        print("Please enter a keyword.")
        return

    try:
        with open(TICKET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No tickets found.")
        return

    found = False

    for ticket in content.split(SEPARATOR):
        if "Ticket ID:" in ticket and keyword in ticket.casefold():
            print(ticket.strip())
            print(SEPARATOR)
            found = True

    if not found:
        print("No tickets found for that keyword.")


# Collect customer feedback
def collect_feedback():
    print("\n--- Customer Feedback ---")

    try:
        rating = int(input("Rate your support experience (1-5): "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        return

    if not 1 <= rating <= 5:
        print("Rating must be between 1 and 5.")
        return

    comment = input("Share your feedback (optional): ").strip()

    with open(FEEDBACK_FILE, "a", encoding="utf-8") as file:
        file.write(f"Rating: {rating}/5\n")
        file.write(f"Comment: {comment or 'No comment'}\n")
        file.write(SEPARATOR + "\n")

    print("Thank you! Your feedback has been saved.")


# View saved customer feedback
def view_feedback():
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip():
            print("\n--- Saved Customer Feedback ---")
            print(content)
        else:
            print("No feedback available.")

    except FileNotFoundError:
        print("No feedback has been submitted yet.")


# Calculate average customer rating
def calculate_average_rating():
    ratings = []

    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("Rating:"):
                    try:
                        rating_text = line.split(":", 1)[1].strip()
                        rating = int(rating_text.split("/")[0])

                        if 1 <= rating <= 5:
                            ratings.append(rating)
                    except ValueError:
                        continue

    except FileNotFoundError:
        print("No feedback file found.")
        return

    if not ratings:
        print("No valid customer ratings available.")
        return

    average = sum(ratings) / len(ratings)

    print("\n--- Customer Satisfaction Report ---")
    print(f"Total ratings: {len(ratings)}")
    print(f"Average rating: {average:.2f}/5")

    if average >= 4.5:
        print("Customer satisfaction: Excellent")
    elif average >= 3.5:
        print("Customer satisfaction: Good")
    elif average >= 2.5:
        print("Customer satisfaction: Average")
    else:
        print("Customer satisfaction: Needs improvement")


# Project status report
def project_status_report():
    print("\n========== PROJECT STATUS REPORT ==========")

    print("\n--- Support Ticket Statistics ---")
    ticket_dashboard()

    print("\n--- Customer Satisfaction ---")
    calculate_average_rating()

    print("\n============================================")
