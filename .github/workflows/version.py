import re
import sys

issue_type_to_increment = {
    'chore': 'patch',
    'docs': 'patch',
    'feat': 'major',
    'fix': 'patch',
    'refactor': 'minor',
    'style': 'patch',
    'test': 'patch'
}

def increment_version(current_version, increment_type):
    major, minor, patch = map(int, current_version.split('.'))
    
    if increment_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif increment_type == 'minor':
        minor += 1
        patch = 0
    elif increment_type == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid increment type")
    
    new_version = f"{major}.{minor}.{patch}"
    return new_version

def main():
    try:
        current_version=sys.argv[1]
        is_type=sys.argv[2]
        #print(current_version)
        #print(issue_type)
        #current_version = input("Enter current version (MAJOR.MINOR.PATCH, or leave empty for 0.0.0): ").strip()
        if not current_version:
            current_version = '0.0.0'
        
        issue_type = is_type.strip().lower()
        
        if issue_type in issue_type_to_increment:
            increment_type = issue_type_to_increment[issue_type]
            new_version = increment_version(current_version, increment_type)
            print(new_version)
        else:
            print("Invalid issue type.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
