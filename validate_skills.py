import os
import yaml

def validate():
    success_count = 0
    fail_count = 0
    
    print("🔍 Starting Validation...")
    
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
            
        if "skill.md" in files:
            file_path = os.path.join(root, "skill.md")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                # Split frontmatter
                if content.startswith("---"):
                    parts = content.split("---")
                    if len(parts) >= 3:
                        frontmatter = yaml.safe_load(parts[1])
                        
                        # Check required fields (removed brand)
                        required = ["name", "version", "category", "description"]
                        missing = [field for field in required if field not in frontmatter]
                        
                        if missing:
                            print(f"❌ {file_path}: Missing fields {missing}")
                            fail_count += 1
                        else:
                            success_count += 1
                    else:
                        print(f"❌ {file_path}: Invalid frontmatter structure")
                        fail_count += 1
                else:
                    print(f"❌ {file_path}: No frontmatter found")
                    fail_count += 1
                    
            except Exception as e:
                print(f"❌ {file_path}: Error reading or parsing - {e}")
                fail_count += 1
                
    print(f"\\n📊 Validation Summary:")
    print(f"✅ Passed: {success_count}")
    print(f"❌ Failed: {fail_count}")
    
    return fail_count == 0

if __name__ == "__main__":
    import sys
    if not validate():
        sys.exit(1)
