from llm_groq import query_groq

class AIAgent:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def handle_task(self, task):
        task = task.lower()
        if "describe" in task:
            return self.data_handler.describe()
        elif "columns" in task:
            return self.data_handler.get_columns()
        else:
            context = f"""
Here is a preview of the data:
{self.data_handler.get_sample(5)}

Task: {task}
"""
            return query_groq(context)
