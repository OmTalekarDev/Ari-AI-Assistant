def handle_command(text: str) -> bool:
    """Handle a small set of local commands.

    Returns False when the assistant should exit.
    """
    command = text.lower().strip()

    if not command:
        return True

    if command in {"exit", "quit", "stop", "goodbye"}:
        print("👋 Ari: Goodbye!")
        return False

    if "hello" in command or "hi ari" in command:
        print("🤖 Ari: Hello! How can I help?")
        return True

    print(f"🤖 Ari heard: {text}")
    return True
