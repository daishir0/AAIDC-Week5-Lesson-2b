#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LangGraph Joke Bot (Version 3)

A simple joke-telling bot built with LangGraph.
This version uses OpenAI API to generate jokes instead of pyjokes.
"""

import os
import yaml
from typing import List, Literal, Annotated, Dict, Any
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
from openai import OpenAI

# 1. Load Configuration
def load_config() -> Dict[str, Any]:
    """Load configuration from config.yaml file."""
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return {
            "openai_api_key": "sk-your-api-key-here",
            "model": "gpt-4o-mini",
            "max_tokens": 100,
            "temperature": 0.7
        }

CONFIG = load_config()

# 2. Initialize OpenAI Client
client = OpenAI(api_key=CONFIG["openai_api_key"])

# 3. Define the State
class Joke(BaseModel):
    """A joke with text and category."""
    text: str
    category: str

# Define a custom reducer for the jokes list
def add(existing_list: List[Joke], new_items: List[Joke]) -> List[Joke]:
    """Append new jokes to the existing list."""
    return existing_list + new_items

class JokeState(BaseModel):
    """The state of the joke bot."""
    jokes: Annotated[List[Joke], add] = []
    jokes_choice: Literal["n", "c", "q"] = "n"  # next joke, change category, or quit
    category: str = "programmer"  # programmer, chuck, or dad
    quit: bool = False

# Helper function to get a joke from OpenAI
def get_joke_from_openai(category: str) -> str:
    """Get a joke from OpenAI API based on the category."""
    # Define prompts based on category
    prompts = {
        "programmer": "Tell me a short, funny programming joke. Just the joke, no introduction or explanation.",
        "chuck": "Tell me a short, funny Chuck Norris programmer joke. Just the joke, no introduction or explanation.",
        "dad": "Tell me a short, funny dad joke. Just the joke, no introduction or explanation."
    }
    
    # Use default if category not found
    prompt = prompts.get(category, prompts["programmer"])
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model=CONFIG["model"],
            messages=[
                {"role": "system", "content": "You are a joke bot that tells short, funny jokes. Respond with just the joke text, no additional text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=CONFIG["max_tokens"],
            temperature=CONFIG["temperature"]
        )
        
        # Extract joke text
        joke_text = response.choices[0].message.content.strip()
        return joke_text
    
    except Exception as e:
        print(f"Error getting joke from OpenAI: {e}")
        return f"Sorry, I couldn't generate a joke. Error: {str(e)[:50]}..."

# 4. Write Node Functions
def show_menu(state: JokeState) -> dict:
    """Display menu and get user input."""
    print(f"🎭 Menu | Category: {state.category.upper()} | Jokes: {len(state.jokes)}")
    print("--------------------------------------------------")
    print("Pick an option:")
    print("[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit")
    user_input = input("User Input: ").strip().lower()
    
    # Map numeric inputs to choices
    input_map = {
        "1": "n",
        "2": "c",
        "3": "q"
    }
    
    # Convert numeric input to letter choice if applicable
    if user_input in input_map:
        user_input = input_map[user_input]
    
    # Validate input
    if user_input not in ["n", "c", "q"]:
        print("\n❌ Invalid option. Please use n, c, or q.\n")
        user_input = "n"  # Default to next joke for invalid inputs
        
    return {"jokes_choice": user_input}

def fetch_joke(state: JokeState) -> dict:
    """Fetch a joke and add it to the state."""
    print("\n⏳ Generating joke using AI...\n")
    joke_text = get_joke_from_openai(state.category)
    new_joke = Joke(text=joke_text, category=state.category)
    print(f"\n😂 {joke_text}\n")
    return {"jokes": [new_joke]}

def update_category(state: JokeState) -> dict:
    """Update the joke category."""
    categories = ["programmer", "chuck", "dad"]
    print("\n📂 Available categories:")
    for i, cat in enumerate(categories):
        print(f"[{i}] {cat}")
    selection = int(input(f"Select category [0-{len(categories)-1}]: ").strip())
    if 0 <= selection < len(categories):
        selected_category = categories[selection]
        print(f"\n✅ Category updated to: {selected_category.upper()}\n")
        return {"category": selected_category}
    else:
        print("\n❌ Invalid selection. Keeping current category.\n")
        return {}

def exit_bot(state: JokeState) -> dict:
    """Exit the joke bot."""
    print("\n🚪==========================================================🚪")
    print("    GOODBYE!")
    print("============================================================")
    return {"quit": True}

# Router function for conditional edges
def route_choice(state: JokeState) -> str:
    """Route to the next node based on user choice."""
    if state.jokes_choice == "n":
        return "fetch_joke"
    elif state.jokes_choice == "c":
        return "update_category"
    elif state.jokes_choice == "q":
        return "exit_bot"
    return "exit_bot"  # Default to exit if input is invalid

# 5. Create the Graph and Add Nodes + Edges
def build_joke_graph():
    """Build and compile the joke bot graph."""
    workflow = StateGraph(JokeState)

    # Add nodes
    workflow.add_node("show_menu", show_menu)
    workflow.add_node("fetch_joke", fetch_joke)
    workflow.add_node("update_category", update_category)
    workflow.add_node("exit_bot", exit_bot)

    # Set entry point
    workflow.set_entry_point("show_menu")

    # Add conditional edges
    workflow.add_conditional_edges(
        "show_menu",
        route_choice,
        {
            "fetch_joke": "fetch_joke",
            "update_category": "update_category",
            "exit_bot": "exit_bot",
        }
    )

    # Add regular edges
    workflow.add_edge("fetch_joke", "show_menu")
    workflow.add_edge("update_category", "show_menu")
    workflow.add_edge("exit_bot", END)

    return workflow.compile()

# 6. Run the Graph
def main():
    """Main function to run the joke bot."""
    print("\n🎉==========================================================🎉")
    print("    WELCOME TO THE LANGGRAPH JOKE BOT (VERSION 3)!")
    print("    This version uses OpenAI API to generate jokes")
    print("============================================================\n")

    # Check if API key is set
    if CONFIG["openai_api_key"] == "sk-your-api-key-here":
        print("⚠️  WARNING: Default API key is being used.")
        print("    Please update the 'openai_api_key' in config.yaml")
        print("    with your actual OpenAI API key.\n")
        proceed = input("Do you want to proceed anyway? (y/n): ").strip().lower()
        if proceed != "y":
            print("Exiting...")
            return

    print("\n🚀==========================================================🚀")
    print("    STARTING JOKE BOT SESSION...")
    print("============================================================")

    # Build and run the graph
    graph = build_joke_graph()
    final_state = graph.invoke(JokeState(), config={"recursion_limit": 100})

    # Show session summary
    print("\n🎊==========================================================🎊")
    print("    SESSION COMPLETE!")
    print("============================================================")
    print(f"    📈 You enjoyed {len(final_state['jokes'])} jokes during this session!")
    print(f"    📂 Final category: {final_state['category'].upper()}")
    print("    🙏 Thanks for using the LangGraph Joke Bot!")
    print("============================================================")

if __name__ == "__main__":
    main()