docs = [
    {
        "text" : "hey",
        "source": "hello",
        "page_number" : 1
    },
    {
        "text" : "hi",
        "source": "hjk",
        "page_number" : 2
    },
    {
        "text" : "su",
        "source": "lulu",
        "page_number" : 3
    }
]

print(docs[1]["text"])
print(docs[-1]["source"])
docs.append({"text" : "New Info"})
print(docs)


chunks = [
    {"text": "This is a valid chunk", "source": "doc1"},
    {"text": " ", "source": "doc2"}, # Too short
    {"text": "Another valid chunk", "source": "doc3"},
    {"text": "Short", "source": "doc4"}
]

valid_chunks = []
doc1_chunks = []
for chunk in chunks:
    if len(chunk["text"]) > 10:
        valid_chunks.append(chunk)
    if chunk["source"] == "doc1":
        doc1_chunks.append(chunk)
print(valid_chunks)
print(doc1_chunks)

doc = {
    "text": "Important info",
    "metadata": {
        "author": "Jane Doe",
        "year": 2024,
        "tags": ["finance", "report"]
    }
}

print(doc["metadata"]["year"])
print(doc["metadata"]["tags"].index("finance") != -1)

def split_text(text, max_length):
     words = text.split(" ")
     chunks = []
     current = ""
     for word in words:
        # len("Hey") + len("") + 1 <= 6
        # 3 + 0 <= 6 True
        # 3 + 4 <= True
        if len(word) + len(current) + 1 <= max_length:
            current += (" " + word) if current else word
        else:
            if current: chunks.append(current)
            current = word
     return chunks
res = split_text("Hey, How is your mother Peti Mama", 6)
print(res)