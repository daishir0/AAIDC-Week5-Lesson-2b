#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LangGraph Joke Bot (Version 1)

A simple joke-telling bot built with LangGraph.
This version adds language switching functionality.
"""

from typing import List, Literal, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
import pyjokes

# 1. Define the State
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
    jokes_choice: Literal["n", "c", "l", "q"] = "n"  # next joke, change category, change language, or quit
    category: str = "neutral"
    language: str = "en"
    quit: bool = False

# Helper function to get a joke from pyjokes
def get_joke(language: str, category: str) -> str:
    """Get a joke from pyjokes library."""
    return pyjokes.get_joke(language=language, category=category)

# 2. Write Node Functions
def show_menu(state: JokeState) -> dict:
    """Display menu and get user input."""
    print(f"🎭 Menu | Category: {state.category.upper()} | Language: {state.language.upper()} | Jokes: {len(state.jokes)}")
    print("--------------------------------------------------")
    print("Pick an option:")
    print("[n] 🎭 Next Joke  [c] 📂 Change Category  [l] 🌐 Change Language  [q] 🚪 Quit")
    user_input = input("User Input: ").strip().lower()
    
    # Map numeric inputs to choices
    input_map = {
        "1": "n",
        "2": "c",
        "3": "l",
        "4": "q"
    }
    
    # Convert numeric input to letter choice if applicable
    if user_input in input_map:
        user_input = input_map[user_input]
    
    # Validate input
    if user_input not in ["n", "c", "l", "q"]:
        print("\n❌ Invalid option. Please use n, c, l, or q.\n")
        user_input = "n"  # Default to next joke for invalid inputs
        
    return {"jokes_choice": user_input}

def fetch_joke(state: JokeState) -> dict:
    """Fetch a joke and add it to the state."""
    joke_text = get_joke(language=state.language, category=state.category)
    new_joke = Joke(text=joke_text, category=state.category)
    print(f"\n😂 {joke_text}\n")
    return {"jokes": [new_joke]}

def update_category(state: JokeState) -> dict:
    """Update the joke category."""
    categories = ["neutral", "chuck", "all"]
    print("\n📂 Available categories:")
    for i, cat in enumerate(categories):
        print(f"[{i}] {cat}")
    selection = int(input("Select category [0-2]: ").strip())
    if 0 <= selection < len(categories):
        selected_category = categories[selection]
        print(f"\n✅ Category updated to: {selected_category.upper()}\n")
        return {"category": selected_category}
    else:
        print("\n❌ Invalid selection. Keeping current category.\n")
        return {}

def update_language(state: JokeState) -> dict:
    """Update the joke language."""
    languages = [
        ("en", "English"),
        ("de", "German"),
        ("es", "Spanish"),
        ("it", "Italian"),
        ("fr", "French")
    ]
    
    print("\n🌐 Available languages:")
    for i, (code, name) in enumerate(languages):
        print(f"[{i}] {name} ({code})")
    
    selection = int(input(f"Select language [0-{len(languages)-1}]: ").strip())
    
    if 0 <= selection < len(languages):
        selected_language = languages[selection][0]
        print(f"\n✅ Language updated to: {languages[selection][1].upper()}\n")
        return {"language": selected_language}
    else:
        print("\n❌ Invalid selection. Keeping current language.\n")
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
    elif state.jokes_choice == "l":
        return "update_language"
    elif state.jokes_choice == "q":
        return "exit_bot"
    return "exit_bot"  # Default to exit if input is invalid

# 3 & 4. Create the Graph and Add Nodes + Edges
def build_joke_graph():
    """Build and compile the joke bot graph."""
    workflow = StateGraph(JokeState)

    # Add nodes
    workflow.add_node("show_menu", show_menu)
    workflow.add_node("fetch_joke", fetch_joke)
    workflow.add_node("update_category", update_category)
    workflow.add_node("update_language", update_language)
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
            "update_language": "update_language",
            "exit_bot": "exit_bot",
        }
    )

    # Add regular edges
    workflow.add_edge("fetch_joke", "show_menu")
    workflow.add_edge("update_category", "show_menu")
    workflow.add_edge("update_language", "show_menu")
    workflow.add_edge("exit_bot", END)

    return workflow.compile()

# 5. Run the Graph
def main():
    """Main function to run the joke bot."""
    print("\n🎉==========================================================🎉")
    print("    WELCOME TO THE LANGGRAPH JOKE BOT (VERSION 1)!")
    print("    This version adds language switching functionality")
    print("============================================================\n")

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
    print(f"    🌐 Final language: {final_state['language'].upper()}")
    print("    🙏 Thanks for using the LangGraph Joke Bot!")
    print("============================================================")

if __name__ == "__main__":
    main()