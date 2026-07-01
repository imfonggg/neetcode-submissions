class TextProcessor:
    # Implement method overloading for format_text method

    def format_text(self, t1: str, t2: str = None) -> str:
        if t2 is None:
            return t1.upper()
        return t1 + t2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
