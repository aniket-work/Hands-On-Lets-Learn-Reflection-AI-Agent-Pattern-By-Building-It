#!/bin/bash

# Create root structure
mkdir -p {config,src/codecollab/core,src/codecollab/utils,tests,scripts,assets/config/prompts}

# Create base files
touch {README.md,LICENSE,pyproject.toml,requirements.txt,setup.cfg}

# Create config files
touch config/{settings.yaml,constants.py}
touch config/prompts/{developer_prompt.j2,tester_prompt.j2}

# Create core code files
touch src/core/{__init__.py,agents.py,orchestrator.py}

# Create utility files
touch src/utils/{__init__.py,loggers.py,helpers.py,llm.py}

# Create test files
touch tests/{__init__.py,test_agents.py,test_orchestrator.py}

# Create assets
touch assets/emoji_mapping.json

# Create git related files
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "*.pyo" >> .gitignore
echo ".env" >> .gitignore
echo ".venv/" >> .gitignore

# Create virtual environment
python -m venv .venv

echo "Project structure created successfully!"