# Agentic Placement Guidance System

An AI-powered placement guidance system that helps students make better placement-related decisions using historical placement data, company information, eligibility criteria, required skills, and placement documents.

The system combines structured data stored in PostgreSQL with unstructured placement documents processed using RAG (Retrieval-Augmented Generation) and an AI agent.

---

## 🚀 Project Overview

The Agentic Placement Guidance System acts as an AI placement mentor for students.

It can provide information such as:

- Student placement statistics
- Company placement history
- Average and highest salary packages
- Companies that visited the college
- Company eligibility criteria
- Required skills for different roles
- Student skill-gap analysis
- Company and role recommendations
- Interview preparation
- Online Assessment (OA) preparation
- Resume guidance
- Placement-related questions using natural language
- Information from placement PDFs and other documents

---

## 🏗️ System Architecture

```text
                    React Frontend
                          |
                          v
                    FastAPI Backend
                          |
                          v
                  AI Agent / Orchestrator
                     /            \
                    /              \
                   v                v
            PostgreSQL             FAISS
          Structured Data      Unstructured Data
                |                    |
                |                    |
        Student Information      Placement PDFs
        Company Information      Interview Experiences
        Placement Records        OA Questions
        Skills & Roles            HR Guidelines
        Eligibility Data          Resume Tips