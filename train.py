from model.qa_model import QAModel
from utils.preprocessing import clean_text

def load_data():
    print("Loading data...")
    context = "This is a sample technical manual."
    question = "What is this?"
    return context, question

def train():
    print("Starting training...")

    model = QAModel()

    context, question = load_data()

    context = clean_text(context)

    print("Question:", question)
    print("Context:", context)

    print("Training completed!")

if __name__ == "__main__":
    train()
