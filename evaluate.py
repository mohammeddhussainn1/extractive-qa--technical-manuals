from model.qa_model import QAModel
from utils.preprocessing import clean_text

def evaluate():
    print("Starting evaluation...")

    model = QAModel()

    context = """
    A router is a networking device that forwards data packets between computer networks.
    Routers perform traffic directing functions on the Internet.
    """

    question = "What is a router?"

    clean_context = clean_text(context)
    answer = model.answer_question(question, clean_context)

    print("Question:", question)
    print("Predicted Answer:", answer)
    print("Evaluation completed!")

if __name__ == "__main__":
    evaluate()
