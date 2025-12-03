import json

# Replace with your actual file name
notebook_filename = "Siamese_Resume_Screener.ipynb"

try:
    # 1. Open the file as raw text
    with open(notebook_filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. Check and delete the broken 'widgets' key
    if "metadata" in data and "widgets" in data["metadata"]:
        print("Found broken 'widgets' metadata. Deleting it...")
        del data["metadata"]["widgets"]
        
        # 3. Save the fixed file
        with open(notebook_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
        print("✅ Success! You can now open the notebook.")
        
    else:
        print("ℹ️ No 'widgets' metadata found. The file might already be clean.")

except Exception as e:
    print(f"Error: {e}")