try:
    import flask
    print("Flask imported successfully")

except ModuleNotFoundError as e:
    print("Error: ", e)