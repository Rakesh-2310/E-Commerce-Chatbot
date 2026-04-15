from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from config import *


# Load embedding model (same as before internally used by semantic_router)
model = SentenceTransformer(EMBEDDING_MODEL)

# -----------------------------
# Define Routes (same as yours)
# -----------------------------
routes = {
    "faq": [
        "What is the return policy?",
        "How can I return a product?",
        "Can I return a product if I don't like it?",
        "What is your refund policy?",
        "How long does it take to receive a refund?",
        "How do refunds work?",
        "How many days does refund processing take?",
        "Can I get a refund for a defective product?",
        "What happens if my item arrives damaged?",
        "What should I do if the product is defective?",
        "Can I exchange a product instead of returning it?",
        "Is there a warranty for defective products?",
        "How do I start a return request?",
        "Where do I submit a return request?",
        "Can I return an item after delivery?",
        "What is the time limit for returns?",
        "How do I track my order?",
        "Where can I check the delivery status?",
        "How can I see my order status?",
        "How do I know when my order will arrive?",
        "Is there a tracking link for my shipment?",
        "Can I track my shipment online?",
        "How do I check my delivery progress?",
        "What payment options do you accept?",
        "Can I pay with a credit card?",
        "Do you support debit card payments?",
        "Can I pay using UPI?",
        "Is cash on delivery available?",
        "Do you accept net banking?",
        "What payment methods are available?",
        "How do I cancel my order?",
        "Can I cancel my order after placing it?",
        "What happens if I cancel an order?",
        "Is there a cancellation fee?",
        "How do I contact customer support?"
    ],
    "sql": [
        "Show me Nike shoes with a 50 percent discount",
        "Find shoes under 3000 rupees",
        "List Puma running shoes",
        "Show shoes with rating above 4.5",
        "Find the cheapest shoes available",
        "Show top rated shoes",
        "Give me shoes with the highest ratings",
        "List shoes with more than 500 reviews",
        "Show products with discount greater than 40 percent",
        "Find shoes priced between 1000 and 5000",
        "Show Puma shoes under 4000 rupees",
        "List Adidas running shoes",
        "Find Nike shoes below 2500",
        "Show top 3 shoes sorted by rating",
        "Give me the most popular shoes",
        "List products sorted by rating",
        "Show the cheapest Puma shoes",
        "Find shoes with at least 4 star rating",
        "List running shoes under 5000",
        "Show discounted shoes",
        "Find shoes with maximum discount",
        "Which shoes have the best ratings?",
        "Show shoes with price less than 2000",
        "Give me shoes with good reviews",
        "Find shoes between 2000 and 4000",
        "List products sorted by price",
        "Show shoes with high ratings and many reviews",
        "Find shoes with rating greater than 4",
        "List all Puma shoes",
        "Show shoes available under budget 3000"
    ]
}

# -----------------------------
# Precompute embeddings
# -----------------------------
route_embeddings = {
    route: model.encode(utterances)
    for route, utterances in routes.items()
}

# -----------------------------
# Routing Function
# -----------------------------
def route_query(query: str, threshold: float = 0.5):
    query_emb = model.encode([query])

    scores = {}

    for route, emb in route_embeddings.items():
        similarity = cosine_similarity(query_emb, emb)
        scores[route] = np.max(similarity)

    best_route = max(scores, key=scores.get)

    # Optional: threshold check (avoid wrong routing)
    if scores[best_route] < threshold:
        return "fallback"

    return best_route


# -----------------------------
# Test (same as your previous)
# -----------------------------
if __name__ == "__main__":
    print(route_query("what about cancel the product "))  # faq
    print(route_query("show shoes under 4000 with best review for sports related"))  # sql