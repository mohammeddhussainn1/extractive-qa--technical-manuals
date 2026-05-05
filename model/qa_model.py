class QAModel:
    def __init__(self):
        self.model_name = "Rule-Based Extractive QA Model"
        print(f"{self.model_name} initialized")

    def answer_question(self, question, context):
        question = question.lower()
        context = context.strip()

        if "router" in question:
            return self.extract_sentence(context, "router")

        if "network" in question:
            return self.extract_sentence(context, "network")

        if "manual" in question:
            return self.extract_sentence(context, "manual")

        return "Answer not found in the provided context."

    def extract_sentence(self, context, keyword):
        sentences = context.split(".")

        for sentence in sentences:
            if keyword in sentence.lower():
                return sentence.strip() + "."

        return "No matching sentence found."
