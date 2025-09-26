members_dict = {'information_node': 'Specialised agent to provide information related to availability of doctors or any FAQs related to the hospital',
                'booking_node': 'Specialised agent only to booj, cancel or reschedule appointments'}

options = list(members_dict.keys()) + ["FINISH"]

worker_info = '\n\n'.join([f'WORKER: {member} \n DESCRIPTION: {description}' for member, description in members_dict.items()]) + '\n\n WORKER: FINISH \nDESCRIPTION: If the user query is answered and routed to finshed'

system_prompt = (
    "You are a supervisor tasked with managing a conversation between following workers."
    "### SPECIALISED ASSISTANT: \n"
    f"{worker_info}\n\n"
    "Your primary role is to help the user make an appointment with the doctor and provide updates on FAQs and doctor's availability"
    "If a customer requests to know the availability of a doctor or to book, reschedule, or cancel an appointment,"
    " delegate the task to the appropriate specialized workers. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH"
    "UTILIZE last conversations to assess if the conversation should end. If you answered the query, route it to FINISH"
)

