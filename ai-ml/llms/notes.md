# Large Language Models (LLMs)

> 📅 Last Updated: 2026-03-23

---

## 📖 Overview

Large Language Models are neural networks trained on vast amounts of text data, capable of understanding and generating human-like text. They power applications like ChatGPT, Claude, and GitHub Copilot.

> "LLMs are trained on the next token prediction task, but they emerge with reasoning capabilities."

---

## 🏗️ Core Architecture

### Transformer (Self-Attention)

The Transformer architecture (Vaswani et al., 2017) uses **self-attention** to weigh the importance of different words in relation to each other.

```python
# Simplified attention mechanism
def attention(Q, K, V):
    """Attention(Q, K, V) = softmax(QK^T / √d_k) V"""
    scores = torch.matmul(Q, K.transpose(-2, -1)) / sqrt(d_k)
    weights = softmax(scores, dim=-1)
    return torch.matmul(weights, V)
```

### Key Components

| Component | Purpose |
|-----------|---------|
| Embeddings | Convert tokens to vectors |
| Self-Attention | Capture relationships between tokens |
| Feed-Forward | Process each token independently |
| Layer Normalization | Stabilize training |
| Positional Encoding | Preserve word order |

---

## 💻 Using LLMs

### OpenAI API

```python
import openai

client = openai.OpenAI(api_key="your-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain LLMs in simple terms."}
    ]
)

print(response.choices[0].message.content)
```

### Anthropic Claude API

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(message.content)
```

---

## 🎯 Prompt Engineering Best Practices

### 1. Be Specific

❌ Bad: "Write code for a function"

✅ Good: "Write a Python function that takes a list of integers and returns the maximum value, with error handling for empty lists."

### 2. Provide Examples (Few-Shot)

```python
# Prompt with examples
"""
Input: 2 + 2
Output: 4

Input: 5 * 3
Output: 15

Input: 10 / 2
Output: ?
"""
```

### 3. Chain of Thought

```python
# Explicit reasoning
"""
Q: If I have 3 apples and give away 1, then buy 5 more, how many do I have?

Let me think step by step:
- Start with 3 apples
- Give away 1: 3 - 1 = 2
- Buy 5: 2 + 5 = 7

Answer: 7
"""
```

---

## 🧪 Common Patterns

### RAG (Retrieval-Augmented Generation)

```python
# 1. Retrieve relevant documents
relevant_docs = search(query="What is attention?", top_k=5)

# 2. Build prompt with context
prompt = f"""
Context:
{chr(10).join(relevant_docs)}

Question: {query}

Answer:
"""

# 3. Generate response
response = llm.generate(prompt)
```

### Function Calling

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    }]
)
```

---

## 📊 Popular LLMs

| Model | Params | Context Window | Strength |
|-------|--------|---------------|----------|
| GPT-4 | ~1.76T | 128K | General purpose |
| Claude 3 Sonnet | — | 200K | Long context |
| Llama 3 70B | 70B | 8K | Open source |
| Mistral Large | — | 32K | Efficient |

---

## ⚠️ Limitations & Risks

| Issue | Description |
|-------|-------------|
| Hallucination | Generating false information confidently |
| Bias | Reflecting biases in training data |
| Context Window | Limited memory of conversation |
| Cost | API usage can be expensive |
| Privacy | Sensitive data sent to external servers |

---

## 🚀 Applications

- **Code Generation** — GitHub Copilot, Codeium
- **Question Answering** — Customer support bots
- **Content Creation** — Writing, summarization
- **Data Analysis** — Structured extraction from text
- **Translation** — Multilingual communication

---

## ❓ Questions & Confusions

- [ ] How does temperature affect output randomness?
- [ ] What's the difference between fine-tuning vs. RAG?

---

## 🔗 Further Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [OpenAI Documentation](https://platform.openai.com/docs/)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)

---

*[← AI & ML](../ai-ml/) · [Back to Index](../../README.md)]*
