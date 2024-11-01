import os

# Define the folder structure as a nested dictionary
folders = {
    "containers": {
        "Dockerfiles": {}
    },
    "pipelines": {
        "jenkins": {},
        "github_actions": {}
    },
    "infrastructure": {
        "ansible_playbooks": {}
    },
    "monitoring": {
        "prometheus_config": {},
        "grafana_dashboards": {}
    }
}

# Helper function to create directories recursively
def create_folders(base_path, structure):
    for folder, subfolders in structure.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")
        create_folders(path, subfolders)

def main():
    # Base project folder name
    base_path = "decentralized-cicd-platform"
    
    # Create the base folder
    os.makedirs(base_path, exist_ok=True)
    print(f"Created: {base_path}")

    # Create the folder hierarchy
    create_folders(base_path, folders)

    # Create README.md in the root directory
    readme_path = os.path.join(base_path, "README.md")
    with open(readme_path, "w") as f:
        f.write("# Decentralized CI/CD Platform\n\n")
        f.write("This project demonstrates a decentralized approach to CI/CD using IPFS, Jenkins, Kubernetes, Ansible, and more.")
    print(f"Created: {readme_path}")

if __name__ == "__main__":
    main()
