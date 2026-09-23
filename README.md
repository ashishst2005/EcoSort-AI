# ♻️ EcoSort AI

### AI-Powered Multimodal Waste Segregation & Sustainable Disposal Assistant

EcoSort AI is an AI-powered waste-management assistant designed to help users identify waste items, understand their appropriate waste category, and obtain source-grounded information about responsible handling and disposal.

The system combines **Retrieval-Augmented Generation (RAG)**, **IBM Granite**, **multimodal/image analysis**, **official Indian waste-management documents**, and a **Streamlit web interface**.

The objective is to make reliable waste-management information more accessible while reducing unsupported AI-generated recommendations.

---

## 📌 Project Overview

Waste segregation is an important part of sustainable waste management. However, individuals may not always know whether an item belongs to wet waste, dry waste, recyclable waste, e-waste, sanitary waste, domestic hazardous waste, or another category.

EcoSort AI addresses this problem by providing an AI-assisted interface where users can:

- Ask questions about waste items
- Upload an image of a waste item
- Identify the item using image analysis
- Retrieve relevant information from official waste-management documents
- Generate a grounded response using IBM Granite
- View the documents and pages used to generate the response
- Receive uncertainty messages when the system does not have sufficient information

The project follows a **knowledge-grounded AI approach** rather than relying solely on the language model's pre-trained knowledge.

---

# 🎯 Problem Statement

Waste segregation and responsible disposal can be difficult for individuals because information about different waste categories and handling practices is often scattered across government guidelines, rules, and technical documents.

Users may also receive incorrect or unsupported information from general-purpose AI systems.

### Problem

> How might we use artificial intelligence to help individuals identify, segregate, and understand the responsible handling of waste using reliable and source-grounded information?

### Proposed Solution

EcoSort AI combines:

```text
User Question / Image
        ↓
Item Identification
        ↓
Knowledge Retrieval
        ↓
Official Waste Documents
        ↓
IBM Granite
        ↓
Grounded Response
        ↓
Sources + Explanation
