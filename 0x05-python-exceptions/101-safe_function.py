#!/usr/bin/python3
def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        import sys
        print(f"Exception: {e}", file=sys.stderr)
    finally:
        return result
