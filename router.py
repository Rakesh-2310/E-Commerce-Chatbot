from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder()

faq = Route(
    name='faq',
    utterances=[
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
    ]
)

sql = Route(
    name='sql',
    utterances=[
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
)

# Create router first
router = SemanticRouter(encoder=encoder)

# Then add routes - this initializes the index
router.add([faq, sql])

test_data = [
    # FAQ queries
    ("What is your policy on defective product?", "faq"),
    ("Can I return a defective item?", "faq"),
    ("How do I return a product?", "faq"),
    ("What is the refund policy?", "faq"),
    ("How long does it take to get my refund?", "faq"),
    ("Can I get a refund if the item is damaged?", "faq"),
    ("How do I track my shipment?", "faq"),
    ("Where can I track my order?", "faq"),
    ("What payment methods do you support?", "faq"),
    ("Do you accept credit cards?", "faq"),
    ("Can I pay using UPI?", "faq"),
    ("Is cash on delivery available?", "faq"),
    ("How many days does refund processing take?", "faq"),
    ("What should I do if my product arrives damaged?", "faq"),
    ("How do I check my order status?", "faq"),

    # SQL queries (product search)
    ("Pink Puma shoes in price range 5000 to 1000", "sql"),
    ("Show me Puma shoes between 1000 and 5000", "sql"),
    ("Find Nike shoes with 50 percent discount", "sql"),
    ("Show shoes under 3000 rupees", "sql"),
    ("List Puma running shoes", "sql"),
    ("What is the price of Nike running shoes?", "sql"),
    ("Show top 3 shoes by rating", "sql"),
    ("Find shoes with rating above 4.5", "sql"),
    ("List shoes with more than 500 reviews", "sql"),
    ("Find shoes cheaper than 2000 rupees", "sql"),
    ("Show the most popular shoes", "sql"),
    ("List Adidas running shoes", "sql"),
    ("Show shoes with discount greater than 40 percent", "sql"),
    ("Which shoes have the highest ratings?", "sql"),
    ("Give me shoes under 2500 with good ratings", "sql"),
]

X, y = zip(*test_data)
router.fit(X=X, y=y)


if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)